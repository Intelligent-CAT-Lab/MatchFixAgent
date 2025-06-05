import sys
import pydot


def parse_nodes_edges(graph):
    """
    Given a pydot Graph or Subgraph, return:
      - nodes: dict mapping original_node_id (str) → label (str) (preserving newlines)
      - edges: list of tuples (src_id, dst_id, edge_label)
    Only considers nodes and edges directly under this graph (ignores nested subgraphs).
    """
    nodes = {}
    for node in graph.get_nodes():
        name = node.get_name().strip('"')
        if not name.isdigit():
            continue
        raw_label = node.get_attributes().get("label", "")
        label = raw_label.strip('"').rstrip()
        nodes[name] = label

    edges = []
    for edge in graph.get_edges():
        src = edge.get_source().strip('"')
        dst = edge.get_destination().strip('"')
        if not (src.isdigit() and dst.isdigit()):
            continue
        raw_elabel = edge.get_attributes().get("label", "").strip('"')
        elabel = raw_elabel.replace("\n", " ").rstrip()
        edges.append((src, dst, elabel))

    return nodes, edges


def build_pred_succ(nodes, edges):
    """
    Build predecessor and successor maps for the given nodes and edges.
    preds[orig] = list of (pred_orig, edge_label)
    succs[orig] = list of (succ_orig, edge_label)
    """
    preds = {nid: [] for nid in nodes}
    succs = {nid: [] for nid in nodes}
    for src, dst, elabel in edges:
        if src in succs and dst in preds:
            succs[src].append((dst, elabel))
            preds[dst].append((src, elabel))
    return preds, succs


def remap_node_ids(nodes, preds):
    """
    Remap original node IDs (strings) to new sequential integers starting at 2,
    reserving 1 for ENTRY. Returns:
      - mapping: dict orig_id → new_int_id
      - entry_orig: list of original IDs chosen as ENTRY successors
    """
    # Find originals with no predecessors
    raw_entries = [nid for nid, plist in preds.items() if not plist]
    if not raw_entries:
        # If all have predecessors (e.g., due to loops), pick the smallest numeric ID
        raw_entries = [min(nodes.keys(), key=lambda x: int(x))]

    entry_orig = sorted(raw_entries, key=int)

    mapping = {}
    next_id = 2
    for orig in sorted(nodes, key=int):
        mapping[orig] = next_id
        next_id += 1

    return mapping, entry_orig


def pretty_print_cfg(nodes, preds, succs, mapping, entry_orig, header_label=None):
    """
    Print the CFG for a single graph (or subgraph), given:
      - nodes, preds, succs: as built above
      - mapping: orig_id → new_id (ENTRY = 1)
      - entry_orig: list of orig_ids for ENTRY successors
      - header_label: optional string to print before the CFG
    """
    if header_label:
        print(f"### CFG for {header_label} ###")
    print("Node 1: ENTRY")
    for idx, orig in enumerate(entry_orig):
        arrow = "└─>" if idx == len(entry_orig) - 1 else "├─>"
        new_id = mapping[orig]
        lines = nodes[orig].split("\n")
        print(f"    {arrow} Node {new_id}: {lines[0]}")
        for extra_line in lines[1:]:
            print(f"        {extra_line}")
    print()

    new_to_orig = {new: orig for orig, new in mapping.items()}
    for new_id in sorted(new_to_orig):
        orig = new_to_orig[new_id]
        lines = nodes[orig].split("\n")
        print(f"Node {new_id}:")
        for line in lines:
            print(f"    {line}")

        children = succs.get(orig, [])
        if children:
            for cidx, (succ_orig, elabel) in enumerate(children):
                arrow = "└─>" if cidx == len(children) - 1 else "├─>"
                succ_new = mapping[succ_orig]
                if elabel:
                    print(f'    {arrow} Node {succ_new} [label="{elabel}"]:')
                else:
                    print(f"    {arrow} Node {succ_new}:")
                succ_lines = nodes[succ_orig].split("\n")
                for succ_line in succ_lines:
                    print(f"        {succ_line}")
        print()
    print("-" * 40)


def get_subgraph_label(subgraph):
    """
    Derive a label for the subgraph. If the subgraph's name starts with 'cluster',
    strip that prefix; otherwise return None.
    """
    name = subgraph.get_name().strip('"')
    if name.startswith("cluster"):
        return name[len("cluster") :]
    return None


def process_graph_recursively(graph):
    """
    Recursively process a pydot Graph or Subgraph (excluding the very top graph):
      - Parse nodes/edges for this graph (excluding nested subgraphs)
      - Build preds/succs, remap IDs, and print CFG
      - For each nested subgraph, recurse
    """
    label = get_subgraph_label(graph)

    nodes, edges = parse_nodes_edges(graph)
    if nodes:
        preds, succs = build_pred_succ(nodes, edges)
        mapping, entry_orig = remap_node_ids(nodes, preds)
        pretty_print_cfg(nodes, preds, succs, mapping, entry_orig, header_label=label)

    for sub in graph.get_subgraphs():
        process_graph_recursively(sub)


def main():
    """
    Reads a DOT description from stdin and prints CFGs for each function-level subgraph.
    Usage:
        python print_cfg.py < example.dot
    """
    dot_data = sys.stdin.read()
    graphs = pydot.graph_from_dot_data(dot_data)
    if not graphs:
        return
    top_graph = graphs[0]

    # Only iterate through subgraphs of the top-level graph (skip printing top-level)
    for sub in top_graph.get_subgraphs():
        process_graph_recursively(sub)


if __name__ == "__main__":
    main()
