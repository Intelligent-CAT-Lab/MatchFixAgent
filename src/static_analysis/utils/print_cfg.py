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
    preds = {nid: [] for nid in nodes}
    succs = {nid: [] for nid in nodes}
    for src, dst, elabel in edges:
        succs[src].append((dst, elabel))
        preds[dst].append((src, elabel))
    return preds, succs


def remap_node_ids(nodes, preds):
    # find originals with no predecessors
    entry_orig = [nid for nid, plist in preds.items() if not plist]
    if not entry_orig:
        entry_orig = [min(nodes.keys(), key=lambda x: int(x))]
    entry_orig = sorted(entry_orig, key=int)
    mapping = {}
    next_id = 2
    for orig in sorted(nodes, key=int):
        mapping[orig] = next_id
        next_id += 1
    return mapping, entry_orig


def get_subgraph_label(graph):
    name = graph.get_name().strip('"')
    if name.startswith("cluster"):
        return name[len("cluster") :]
    return None


def pretty_print_cfg(nodes, preds, succs, mapping, entry_orig, header_label=None):
    if header_label:
        print(f"### CFG for {header_label} ###")
    print("Node 1: ENTRY")
    for idx, orig in enumerate(entry_orig):
        arrow = "└─>" if idx == len(entry_orig) - 1 else "├─>"
        new_id = mapping[orig]
        lines = nodes[orig].split("\n")
        print(f"    {arrow} Node {new_id}: {lines[0]}")
        for extra in lines[1:]:
            print(f"        {extra}")
    print()
    new_to_orig = {new: orig for orig, new in mapping.items()}
    for new_id in sorted(new_to_orig):
        orig = new_to_orig[new_id]
        lines = nodes[orig].split("\n")
        print(f"Node {new_id}:")
        for ln in lines:
            print(f"    {ln}")
        children = succs.get(orig, [])
        if children:
            for cidx, (sorig, el) in enumerate(children):
                arrow = "└─>" if cidx == len(children) - 1 else "├─>"
                sid = mapping[sorig]
                if el:
                    print(f'    {arrow} Node {sid} [label="{el}"]:')
                else:
                    print(f"    {arrow} Node {sid}:")
                for sl in nodes[sorig].split("\n"):
                    print(f"        {sl}")
        print()
    print("-" * 40)


def process_graph_recursively(graph):
    label = get_subgraph_label(graph)
    nodes, edges = parse_nodes_edges(graph)
    if nodes:
        preds, succs = build_pred_succ(nodes, edges)
        mapping, entry_orig = remap_node_ids(nodes, preds)
        pretty_print_cfg(nodes, preds, succs, mapping, entry_orig, header_label=label)
    for sub in graph.get_subgraphs():
        process_graph_recursively(sub)


def main():
    source_code_file = sys.argv[1]
    dot_data_file = sys.argv[2]

    # print source code with line numbers
    with open(source_code_file, "r") as f:
        lines = f.readlines()

    print(f"SOURCE CODE:")
    for idx, line in enumerate(lines, start=1):
        print(f"{idx:4}: {line.rstrip()}")

    print()

    with open(dot_data_file, "r") as f:
        dot_data = f.read()
    graphs = pydot.graph_from_dot_data(dot_data)
    if not graphs:
        return
    top = graphs[0]
    subs = top.get_subgraphs()
    if subs:
        for sub in subs:
            process_graph_recursively(sub)
    else:
        process_graph_recursively(top)


if __name__ == "__main__":
    main()
