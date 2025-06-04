from tree_sitter import Language, Parser
import networkx as nx


class CFGBuilder:
    def __init__(self, root_node, source_code):
        """
        Initialize the CFGBuilder.

        :param root_node: The root Tree-sitter node (typically 'module').
        :param source_code: The entire source code string.
        """
        self.root = root_node
        self.source_code = source_code
        self.lines = source_code.splitlines()
        self.graph = nx.DiGraph()
        self._id_counter = 0
        self.node_labels = {}  # node_id → label string
        self.return_nodes = set()  # node_ids for return statements

        # For loop handling (unused here but kept for completeness)
        self.loop_stack = []

        # Maps for break/continue to their loop header (unused for exceptions)
        self.break_map = {}
        self.continue_map = {}

        # Create special ENTRY and EXIT nodes
        self.entry_id = self._new_node(label="ENTRY")
        self.exit_id = self._new_node(label="EXIT")

    def _new_node(self, ts_node=None, label=None):
        """
        Create a new CFG node with a unique integer ID and store its label.
        If ts_node is provided, prepend the label with the node’s start line number
        and use the full source line as snippet.

        :param ts_node: Tree-sitter node (optional) from which to derive label and line.
        :param label: Explicit label string (optional).
        :return: int node_id
        """
        node_id = self._id_counter
        self._id_counter += 1

        if label is not None:
            self.node_labels[node_id] = label
        elif ts_node is not None:
            start_row, _ = ts_node.start_point
            line_num = start_row + 1
            if 0 <= start_row < len(self.lines):
                snippet = self.lines[start_row].strip()
            else:
                snippet = ts_node.type
            self.node_labels[node_id] = f"(L{line_num}) {snippet}"
        else:
            raise ValueError("Must provide ts_node or label")

        self.graph.add_node(node_id)
        return node_id

    def _is_branching_node(self, node):
        """
        Identify Tree-sitter nodes that create new control-flow:
        if, for, while, try, match, break, continue, return.
        """
        return node.type in {
            "if_statement",
            "for_statement",
            "while_statement",
            "try_statement",
            "match_statement",
            "break_statement",
            "continue_statement",
            "return_statement",
        }

    def build(self):
        """
        Build the CFG for the entire parsed file. Finds all function definitions;
        if none, treats the module body as one big block.
        Finally, links ENTRY → first‐level branching nodes and all exit nodes → EXIT.
        """
        func_defs = self._find_functions(self.root)
        all_entries = set()
        all_exits = set()

        if func_defs:
            for func in func_defs:
                body = func.child_by_field_name("body")
                if body:
                    e_ids, x_ids = self._build_block(list(body.named_children))
                    all_entries.update(e_ids)
                    all_exits.update(x_ids)
        else:
            e_ids, x_ids = self._build_block(list(self.root.named_children))
            all_entries.update(e_ids)
            all_exits.update(x_ids)

        # Connect ENTRY ➔ each first branching node (if any)
        if all_entries:
            for eid in all_entries:
                self.graph.add_edge(self.entry_id, eid)
        else:
            # No branching at all? Connect ENTRY ➔ EXIT directly
            self.graph.add_edge(self.entry_id, self.exit_id)

        # Connect every exit node ➔ EXIT
        for xid in all_exits:
            self.graph.add_edge(xid, self.exit_id)

    def _find_functions(self, node):
        """
        Recursively collect all 'function_definition' nodes in the tree,
        including those nested under 'decorated_definition'.
        """
        funcs = []
        if node.type == "function_definition":
            funcs.append(node)
        elif node.type == "decorated_definition":
            for c in node.named_children:
                if c.type == "function_definition":
                    funcs.append(c)
                    break
        else:
            for c in node.named_children:
                funcs.extend(self._find_functions(c))
        return funcs

    def _build_block(self, stmts):
        """
        Build CFG for a sequential block of statements.
        Returns (entry_node_ids, exit_node_ids).
        """
        entry_nodes = set()
        exit_nodes = set()
        prev_exits = set()
        saw_branch = False

        for stmt in stmts:
            if self._is_branching_node(stmt):
                sub_entries, sub_exits = self._build_branching(stmt)

                if not saw_branch:
                    entry_nodes.update(sub_entries)
                    saw_branch = True

                # Link every previous exit to each new sub-entry (skip returns)
                for pe in prev_exits:
                    if pe in self.return_nodes:
                        continue
                    for se in sub_entries:
                        self.graph.add_edge(pe, se)

                # Partition sub_exits into "fallthrough" vs. "special" (returns)
                fallthrough = set()
                special = set()
                for e in sub_exits:
                    if e in self.return_nodes:
                        special.add(e)
                    else:
                        fallthrough.add(e)

                exit_nodes.update(special)
                prev_exits = fallthrough

                # If nothing falls through, we cannot continue in this block
                if not prev_exits:
                    break
            else:
                # Non-branching: no CFG node created, just flow-through
                continue

        # Whatever remains in prev_exits becomes exit of this block
        exit_nodes.update(prev_exits)
        return entry_nodes, exit_nodes

    def _build_branching(self, node):
        """
        Dispatch to the appropriate handler based on node.type.
        """
        if node.type == "if_statement":
            return self._build_if(node)
        elif node.type in {"for_statement", "while_statement"}:
            return self._build_loop(node)
        elif node.type == "try_statement":
            return self._build_try(node)
        elif node.type == "match_statement":
            return self._build_match(node)
        elif node.type == "break_statement":
            return self._build_break(node)
        elif node.type == "continue_statement":
            return self._build_continue(node)
        elif node.type == "return_statement":
            return self._build_return(node)
        else:
            # For any unhandled branching, label it and treat as both entry & exit
            nid = self._new_node(ts_node=node)
            return {nid}, {nid}

    def _build_if(self, node):
        """
        Build CFG for an if-elif-else chain.
        """
        cond_ids = []
        body_nodes = []
        else_body = None

        # 1) The "if" condition node
        cond_ids.append(self._new_node(ts_node=node))
        body_nodes.append(node.child_by_field_name("consequence"))

        # 2) Collect "elif" clauses and an optional "else"
        for c in node.named_children:
            if c.type == "elif_clause":
                cond_ids.append(self._new_node(ts_node=c))
                body_nodes.append(c.child_by_field_name("consequence"))
            elif c.type == "else_clause":
                else_body = c.child_by_field_name("body")

        entry_set = {cond_ids[0]}
        exit_set = set()

        # 3) For each condition, link its true‐branch and false‐branch
        for idx, cid in enumerate(cond_ids):
            body = body_nodes[idx]
            # -- True branch --
            if body:
                stmts = list(body.named_children)
                t_entries, t_exits = self._build_block(stmts)
                # If no exits from the block, treat condition itself as fall-through
                if not t_exits:
                    t_exits = {cid}
                if t_entries:
                    for te in t_entries:
                        self.graph.add_edge(cid, te)
                    exit_set.update(t_exits)
                else:
                    # No nested branching in the body: either loop back or exit
                    if self.loop_stack:
                        header = self.loop_stack[-1]
                        self.graph.add_edge(cid, header)
                    else:
                        exit_set.add(cid)
            else:
                exit_set.add(cid)

            # -- False branch --
            if idx + 1 < len(cond_ids):
                # Link false → next "elif"
                self.graph.add_edge(cid, cond_ids[idx + 1])
            else:
                # Last condition: false → else or exit
                if else_body:
                    e_entries, e_exits = self._build_block(list(else_body.named_children))
                    if not e_exits:
                        e_exits = {cid}
                    for ee in e_entries:
                        self.graph.add_edge(cid, ee)
                    exit_set.update(e_exits)
                else:
                    exit_set.add(cid)

        return entry_set, exit_set

    def _build_loop(self, node):
        """
        Build CFG for a for- or while-loop.
        """
        header = self._new_node(ts_node=node)
        self.loop_stack.append(header)

        body = node.child_by_field_name("body")
        b_entries, b_exits = (set(), set())
        if body:
            b_entries, b_exits = self._build_block(list(body.named_children))

        entry_set = {header}
        exit_set = set()

        if b_entries:
            for be in b_entries:
                self.graph.add_edge(header, be)
            for bx in b_exits:
                if bx in self.return_nodes:
                    exit_set.add(bx)
                elif bx in self.break_map and self.break_map[bx] == header:
                    exit_set.add(bx)
                elif bx in self.continue_map and self.continue_map[bx] == header:
                    self.graph.add_edge(bx, header)
                else:
                    self.graph.add_edge(bx, header)
        else:
            # If body has no nested branching, loop back to itself
            self.graph.add_edge(header, header)

        exit_set.add(header)
        self.loop_stack.pop()
        return entry_set, exit_set

    def _build_try(self, node):
        """
        Build CFG for try-except-finally, explicitly including a 'finally' header node.
        Ensures the try-header itself also links to finally for the normal path.
        """
        # 1) Create a 'try' header
        tid = self._new_node(ts_node=node)  # e.g., "(L2) try:"
        entry_set = {tid}
        exit_set = set()

        # 2) Parse the try-body
        try_body = node.child_by_field_name("body")
        t_entries, t_exits = (set(), set())
        if try_body:
            t_entries, t_exits = self._build_block(list(try_body.named_children))
            # If no exits from try-body, treat the try header itself as a fall-through
            if not t_exits:
                t_exits = {tid}
            for te in t_entries:
                self.graph.add_edge(tid, te)
        else:
            # No nested statements under "try": header itself is a fall-through
            t_exits = {tid}

        # 3) Parse all except clauses
        except_clauses = [c for c in node.named_children if c.type == "except_clause"]
        all_except_exits = []
        for ex_clause in except_clauses:
            # Create a header for this "except"
            ex_hdr = self._new_node(ts_node=ex_clause)  # e.g., "(L5) except ZeroDivisionError:"
            ex_body = ex_clause.child_by_field_name("body")
            ex_entries, ex_exits = (set(), set())
            if ex_body:
                ex_entries, ex_exits = self._build_block(list(ex_body.named_children))
                # If no exits from except-body, treat the header as fall-through
                if not ex_exits:
                    ex_exits = {ex_hdr}
                for ee in ex_entries:
                    self.graph.add_edge(ex_hdr, ee)
            else:
                # No nested statements under this except
                ex_exits = {ex_hdr}
            # Link try-header ➔ except-header (exception path)
            self.graph.add_edge(tid, ex_hdr)
            all_except_exits.extend(ex_exits)

        # 4) Identify a finally clause, if present
        finally_clause = None
        for c in node.named_children:
            if c.type == "finally_clause":
                finally_clause = c
                break

        if finally_clause:
            # Create a "finally" header
            fin_hdr = self._new_node(ts_node=finally_clause)  # e.g., "(L8) finally:"
            # Link the try-header itself ➔ finally-header (normal completion path)
            self.graph.add_edge(tid, fin_hdr)
            # Link every normal try exit to fin_hdr
            for te in t_exits:
                self.graph.add_edge(te, fin_hdr)
            # Link every except-body exit to fin_hdr
            for exi in all_except_exits:
                self.graph.add_edge(exi, fin_hdr)

            # Build the finally body under fin_hdr
            fin_body = finally_clause.child_by_field_name("body")
            f_entries, f_exits = (set(), set())
            if fin_body:
                f_entries, f_exits = self._build_block(list(fin_body.named_children))
                # If no exits from finally-body, treat fin_hdr as fall-through
                if not f_exits:
                    f_exits = {fin_hdr}
                for fe in f_entries:
                    self.graph.add_edge(fin_hdr, fe)
            else:
                # No nested statements under "finally"
                f_exits = {fin_hdr}
            exit_set.update(f_exits)
        else:
            # No finally clause at all
            exit_set.update(t_exits)
            exit_set.update(all_except_exits)

        # 5) If there were no except clauses and no try-body entries,
        #    ensure the try-header itself falls through to exit
        if not except_clauses and not t_entries:
            if not finally_clause:
                exit_set.add(tid)

        return entry_set, exit_set

    def _build_match(self, node):
        """
        Build CFG for match-case (Python 3.10+).
        """
        mid = self._new_node(ts_node=node)
        entry_set = {mid}
        exit_set = set()

        for c in node.named_children:
            if c.type == "match_case":
                body = c.child_by_field_name("body")
                if body:
                    e_nodes, e_exits = self._build_block(list(body.named_children))
                    # If no exits from a case, the match header itself is fall-through
                    if not e_exits:
                        e_exits = {mid}
                    for en in e_nodes:
                        self.graph.add_edge(mid, en)
                    exit_set.update(e_exits)
                else:
                    exit_set.add(mid)

        if not exit_set:
            exit_set.add(mid)

        return entry_set, exit_set

    def _build_break(self, node):
        bid = self._new_node(ts_node=node)
        if self.loop_stack:
            self.break_map[bid] = self.loop_stack[-1]
        return {bid}, {bid}

    def _build_continue(self, node):
        cid = self._new_node(ts_node=node)
        if self.loop_stack:
            self.continue_map[cid] = self.loop_stack[-1]
        return {cid}, {cid}

    def _build_return(self, node):
        rid = self._new_node(ts_node=node)
        self.return_nodes.add(rid)
        return {rid}, {rid}

    def print_graph(self):
        """
        Print each node and its successors in a human-readable format.
        """
        for nid in sorted(self.graph.nodes()):
            label = self.node_labels.get(nid, str(nid))
            print(f"Node {nid}: {label}")
            for succ in self.graph.successors(nid):
                slabel = self.node_labels.get(succ, str(succ))
                print(f"    └─> Node {succ}: {slabel}")
            print()


if __name__ == "__main__":

    language = "python"
    source_code = """
def binary_search(arr, low, high, x):

    if high >= low:

        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        return -1
"""

    LANGUAGE = Language("lib/build/my-languages.so", language)
    parser = Parser()
    parser.set_language(LANGUAGE)

    tree = parser.parse(bytes(source_code, "utf8"))

    builder = CFGBuilder(tree.root_node, source_code)
    builder.build()
    builder.print_graph()
