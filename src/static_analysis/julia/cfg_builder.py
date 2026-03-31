"""CFG builder for Julia using tree-sitter.

This builder uses tree-sitter with the tree_sitter_julia bindings to parse
Julia source code and build a control flow graph. If tree-sitter is not
available, it falls back to a naive line-based parser.
"""
from .model import Block, Link, CFG

try:
    from tree_sitter import Language, Parser
    import tree_sitter_julia as tsjulia
except Exception:  # pragma: no cover - optional dependency
    Language = None
    Parser = None
    tsjulia = None


class CFGBuilder:
    def __init__(self, separate=False):
        self.after_loop_block_stack = []
        self.curr_loop_guard_stack = []
        self.current_block = None
        self.separate_node_blocks = separate
        self.src = ""

        try:
            if Language is not None and Parser is not None and tsjulia is not None:
                LANGUAGE = Language(tsjulia.language())
                self.parser = Parser(LANGUAGE)
            else:
                self.parser = None
        except Exception:  # pragma: no cover - handled in tests
            self.parser = None

    # Graph management
    def new_block(self):
        self.current_id += 1
        return Block(self.current_id)

    def add_statement(self, block, statement):
        block.statements.append(statement)

    def add_exit(self, block, nextblock, exitcase=None):
        newlink = Link(block, nextblock, exitcase)
        block.exits.append(newlink)
        nextblock.predecessors.append(newlink)

    def new_loopguard(self):
        if self.current_block.is_empty() and len(self.current_block.exits) == 0:
            loopguard = self.current_block
        else:
            loopguard = self.new_block()
            self.add_exit(self.current_block, loopguard)
        return loopguard

    # Build methods
    def build_from_src(self, name, src):
        if self.parser is not None:
            tree = self.parser.parse(bytes(src, 'utf8'))
            return self.build(name, tree, src)
        # Fallback: naive sequential blocks
        return self._build_simple(name, src)

    def build_from_file(self, name, filepath):
        with open(filepath, 'r') as src_file:
            src = src_file.read()
        cfg = self.build_from_src(name, src)
        return cfg

    def build(self, name, tree, src):
        self.src = src
        self.cfg = CFG(name)
        self.current_id = 0
        self.current_block = self.new_block()
        self.cfg.entryblock = self.current_block
        root = tree.root_node

        # Find function definition
        func_def = None
        for child in root.children:
            if child.type == 'function_definition':
                func_def = child
                break

        if func_def:
            # Visit function body (children after signature)
            self._visit_function_body(func_def)
        else:
            # Visit top-level statements
            for child in root.children:
                self.visit(child)

        self.clean_cfg(self.cfg.entryblock)
        return self.cfg

    def _visit_function_body(self, func_def):
        """Visit the body of a function definition (statements after signature)."""
        in_body = False
        for child in func_def.children:
            if child.type == 'signature':
                in_body = True
                continue
            if child.type == 'end':
                break
            if in_body and child.type not in ('function', 'end'):
                self.visit(child)

    # Utility
    def get_text(self, node):
        return node.text.decode()

    def invert(self, cond_text):
        cond_text = cond_text.strip()
        if cond_text.startswith('!'):
            return cond_text[1:].strip()
        return f'!({cond_text})'

    # Clean cfg
    def clean_cfg(self, block, visited=None):
        if visited is None:
            visited = []
        if block in visited:
            return
        visited.append(block)
        if block.is_empty():
            for pred in list(block.predecessors):
                for exit in list(block.exits):
                    self.add_exit(pred.source, exit.target, exit.exitcase)
                    if exit in exit.target.predecessors:
                        exit.target.predecessors.remove(exit)
                if pred in pred.source.exits:
                    pred.source.exits.remove(pred)
            for exit in list(block.exits):
                self.clean_cfg(exit.target, visited)
            block.predecessors = []
            block.exits = []
        else:
            for exit in list(block.exits):
                self.clean_cfg(exit.target, visited)

    # Visitors
    def visit(self, node):
        method = getattr(self, f'visit_{node.type}', None)
        if method is not None:
            method(node)
        else:
            self.visit_generic(node)

    def visit_generic(self, node):
        self.add_statement(self.current_block, node)
        if self.separate_node_blocks:
            new = self.new_block()
            self.add_exit(self.current_block, new)
            self.current_block = new

    def visit_assignment(self, node):
        self.add_statement(self.current_block, node)
        if self.separate_node_blocks:
            new = self.new_block()
            self.add_exit(self.current_block, new)
            self.current_block = new

    def visit_compound_assignment_expression(self, node):
        self.add_statement(self.current_block, node)
        if self.separate_node_blocks:
            new = self.new_block()
            self.add_exit(self.current_block, new)
            self.current_block = new

    def visit_call_expression(self, node):
        self.add_statement(self.current_block, node)
        if self.separate_node_blocks:
            new = self.new_block()
            self.add_exit(self.current_block, new)
            self.current_block = new

    def visit_if_statement(self, node):
        self.add_statement(self.current_block, node)

        # Find condition (first binary_expression or identifier after 'if')
        cond = None
        for child in node.children:
            if child.type in ('binary_expression', 'identifier', 'call_expression', 'unary_expression'):
                cond = child
                break
        cond_text = self.get_text(cond) if cond else "true"

        if_block = self.new_block()
        self.add_exit(self.current_block, if_block, cond_text)
        after_if = self.new_block()

        # Find else/elseif clauses
        elseif_clauses = [c for c in node.children if c.type == 'elseif_clause']
        else_clause = None
        for c in node.children:
            if c.type == 'else_clause':
                else_clause = c
                break

        # Handle elseif and else
        current_dispatch = self.current_block
        for elseif in elseif_clauses:
            # Create block for this elseif branch
            elseif_block = self.new_block()
            # Find elseif condition
            elseif_cond = None
            for child in elseif.children:
                if child.type in ('binary_expression', 'identifier', 'call_expression', 'unary_expression'):
                    elseif_cond = child
                    break
            elseif_cond_text = self.get_text(elseif_cond) if elseif_cond else "true"

            # Link from previous dispatch to this elseif (when previous condition is false)
            next_dispatch = self.new_block()
            self.add_exit(current_dispatch, next_dispatch, self.invert(cond_text))
            self.add_exit(next_dispatch, elseif_block, elseif_cond_text)

            # Visit elseif body
            self.current_block = elseif_block
            for child in elseif.children:
                if child.type not in ('elseif', 'binary_expression', 'identifier', 'call_expression', 'unary_expression'):
                    self.visit(child)
            if not self.current_block.exits:
                self.add_exit(self.current_block, after_if)

            current_dispatch = next_dispatch
            cond_text = elseif_cond_text

        if else_clause is not None:
            else_block = self.new_block()
            self.add_exit(current_dispatch, else_block, self.invert(cond_text))
            self.current_block = else_block
            for child in else_clause.children:
                if child.type != 'else':
                    self.visit(child)
            if not self.current_block.exits:
                self.add_exit(self.current_block, after_if)
        else:
            self.add_exit(current_dispatch, after_if, self.invert(cond_text))

        # Visit if body (statements after condition, before elseif/else/end)
        self.current_block = if_block
        in_body = False
        for child in node.children:
            if child.type in ('binary_expression', 'identifier', 'call_expression', 'unary_expression') and not in_body:
                in_body = True
                continue
            if child.type in ('elseif_clause', 'else_clause', 'end'):
                break
            if in_body and child.type not in ('if', 'end'):
                self.visit(child)
        if not self.current_block.exits:
            self.add_exit(self.current_block, after_if)

        self.current_block = after_if

    def visit_while_statement(self, node):
        loop_guard = self.new_loopguard()
        self.current_block = loop_guard
        self.add_statement(self.current_block, node)

        # Find condition
        cond = None
        for child in node.children:
            if child.type in ('binary_expression', 'identifier', 'call_expression', 'unary_expression'):
                cond = child
                break
        cond_text = self.get_text(cond) if cond else "true"

        self.curr_loop_guard_stack.append(loop_guard)
        while_block = self.new_block()
        self.add_exit(self.current_block, while_block, cond_text)

        after_while = self.new_block()
        self.after_loop_block_stack.append(after_while)
        self.add_exit(self.current_block, after_while, self.invert(cond_text))

        # Visit body
        self.current_block = while_block
        in_body = False
        for child in node.children:
            if child.type in ('binary_expression', 'identifier', 'call_expression', 'unary_expression') and not in_body:
                in_body = True
                continue
            if child.type == 'end':
                break
            if in_body and child.type not in ('while', 'end'):
                self.visit(child)

        if not self.current_block.exits:
            self.add_exit(self.current_block, loop_guard)

        self.current_block = after_while
        self.after_loop_block_stack.pop()
        self.curr_loop_guard_stack.pop()

    def visit_for_statement(self, node):
        loop_guard = self.new_loopguard()
        self.current_block = loop_guard
        self.add_statement(self.current_block, node)

        # Find for binding (e.g., "i = 1:10" or "i in collection")
        for_binding = None
        for child in node.children:
            if child.type == 'for_binding':
                for_binding = child
                break
        iter_text = self.get_text(for_binding) if for_binding else ""

        self.curr_loop_guard_stack.append(loop_guard)
        for_block = self.new_block()
        self.add_exit(self.current_block, for_block, iter_text)

        after_for = self.new_block()
        self.add_exit(self.current_block, after_for)
        self.after_loop_block_stack.append(after_for)

        # Visit body
        self.current_block = for_block
        in_body = False
        for child in node.children:
            if child.type == 'for_binding':
                in_body = True
                continue
            if child.type == 'end':
                break
            if in_body and child.type not in ('for', 'end'):
                self.visit(child)

        if not self.current_block.exits:
            self.add_exit(self.current_block, loop_guard)

        self.current_block = after_for
        self.after_loop_block_stack.pop()
        self.curr_loop_guard_stack.pop()

    def visit_return_statement(self, node):
        self.add_statement(self.current_block, node)
        self.cfg.finalblocks.append(self.current_block)
        self.current_block = self.new_block()

    def visit_break_statement(self, node):
        if self.after_loop_block_stack:
            self.add_exit(self.current_block, self.after_loop_block_stack[-1])

    def visit_continue_statement(self, node):
        if self.curr_loop_guard_stack:
            self.add_exit(self.current_block, self.curr_loop_guard_stack[-1])

    def visit_function_definition(self, node):
        """Handle nested function definitions."""
        self.add_statement(self.current_block, node)

    def visit_macro_definition(self, node):
        """Handle macro definitions."""
        self.add_statement(self.current_block, node)

    def visit_try_statement(self, node):
        """Handle try-catch-finally blocks."""
        self.add_statement(self.current_block, node)
        after_try = self.new_block()

        # Find try body, catch clause, finally clause
        try_block = self.new_block()
        self.add_exit(self.current_block, try_block)

        # Visit try body
        self.current_block = try_block
        in_body = False
        for child in node.children:
            if child.type == 'try':
                in_body = True
                continue
            if child.type in ('catch_clause', 'finally_clause', 'end'):
                break
            if in_body:
                self.visit(child)

        if not self.current_block.exits:
            self.add_exit(self.current_block, after_try)

        # Handle catch clause
        for child in node.children:
            if child.type == 'catch_clause':
                catch_block = self.new_block()
                self.add_exit(try_block, catch_block, "exception")
                self.current_block = catch_block
                for c in child.children:
                    if c.type not in ('catch',):
                        self.visit(c)
                if not self.current_block.exits:
                    self.add_exit(self.current_block, after_try)

        self.current_block = after_try

    # ------------------------------------------------------------------
    # Fallback implementation
    # ------------------------------------------------------------------
    class _FakeNode:
        """Minimal object mimicking the tree-sitter node API used by Block."""

        def __init__(self, text: str, line: int):
            self.text = text.encode()
            self.type = "statement"
            self.start_point = (line, 0)

    def _build_simple(self, name: str, src: str) -> CFG:
        """Naive CFG builder used when tree-sitter is unavailable."""
        self.cfg = CFG(name)
        self.current_id = 0
        lines = []

        # Find function body between first line and 'end'
        src_lines = src.splitlines()
        start_idx = 0
        end_idx = len(src_lines)

        for i, line in enumerate(src_lines):
            stripped = line.strip()
            if stripped.startswith('function '):
                start_idx = i + 1
            elif stripped == 'end' and i > start_idx:
                end_idx = i
                break

        for ln in range(start_idx, end_idx):
            stripped = src_lines[ln].strip()
            if stripped and stripped != 'end':
                lines.append((ln, stripped))

        prev = None
        for idx, (ln, stmt) in enumerate(lines):
            block = self.new_block()
            block.statements.append(self._FakeNode(stmt, ln))
            if idx == 0:
                self.cfg.entryblock = block
            if prev is not None:
                self.add_exit(prev, block)
            prev = block
        if prev is not None:
            self.cfg.finalblocks.append(prev)
        return self.cfg
