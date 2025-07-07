import networkx as nx
import pydot

# Enhanced multi-language control flow keywords
CONTROL_FLOW_KEYWORDS = {
    "condition": {
        "keywords": ["if ", "switch", "case", "elif", "else if", "else:", "elsif", "when", "match", "select"],
        "operators": ["==", "!=", "<=", ">=", "<", ">", "&&", "||", "and", "or", "is", "in", "not"],
    },
    "loop": {
        "keywords": ["for ", "while ", "do ", "foreach", "until", "loop", "repeat", "range"],
        "patterns": ["in range", "in ", "..", "...", "to ", "downto"],
    },
    "return": {
        "keywords": ["return", "yield", "break", "continue", "exit", "throw", "raise"],
        "patterns": ["return ", "yield ", "throw ", "raise "],
    },
    "function": {
        "keywords": ["def ", "fn ", "function ", "func ", "method ", "proc ", "sub "],
        "modifiers": ["public ", "private ", "protected ", "static ", "async ", "await"],
        "types": ["void ", "int ", "string ", "bool ", "float ", "double ", "char "],
    },
    "assignment": {
        "operators": ["=", ":=", "<-", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", ">>=", "<<="],
        "declarations": ["let ", "var ", "const ", "mut ", "auto ", "final ", "val ", "type "],
        "patterns": ["new ", "make(", "malloc(", "calloc(", "alloc"],
    },
    "error_handling": {
        "keywords": ["try", "catch", "except", "finally", "panic", "recover", "defer"],
        "patterns": ["?", "??", ".unwrap()", ".expect(", "Result<", "Option<"],
    },
}


def extract_all_subgraphs(graph):
    all_graphs = []

    def recurse(g):
        all_graphs.append(nx.nx_pydot.from_pydot(g))
        for subgraph in g.get_subgraphs():
            recurse(subgraph)

    recurse(graph)
    return all_graphs


def parse_dot(dot_str):
    (pydot_graph,) = pydot.graph_from_dot_data(dot_str)
    all_graphs = extract_all_subgraphs(pydot_graph)
    merged_graph = nx.DiGraph()
    for g in all_graphs:
        merged_graph.add_nodes_from(g.nodes(data=True))
        merged_graph.add_edges_from(g.edges(data=True))
    return merged_graph


def get_node_type(label):
    """Enhanced multi-language node type classification"""
    label = label.lower()
    lines = [line.strip() for line in label.splitlines() if line.strip()]

    if not lines:
        return "other"

    # Check for pure single-statement nodes first
    if len(lines) == 1:
        line = lines[0]

        # Pure condition nodes
        if any(keyword in line for keyword in CONTROL_FLOW_KEYWORDS["condition"]["keywords"]):
            return "condition"

        # Pure return nodes
        if any(keyword in line for keyword in CONTROL_FLOW_KEYWORDS["return"]["keywords"]):
            return "return"

        # Pure loop nodes
        if any(keyword in line for keyword in CONTROL_FLOW_KEYWORDS["loop"]["keywords"]):
            return "loop"

    # For multi-line nodes, analyze content distribution
    node_characteristics = {"assignment": 0, "return": 0, "condition": 0, "loop": 0, "function": 0, "error_handling": 0}

    for line in lines:
        # Count assignment indicators
        if (
            any(op in line for op in CONTROL_FLOW_KEYWORDS["assignment"]["operators"])
            or any(kw in line for kw in CONTROL_FLOW_KEYWORDS["assignment"]["declarations"])
            or any(pattern in line for pattern in CONTROL_FLOW_KEYWORDS["assignment"]["patterns"])
        ):
            node_characteristics["assignment"] += 1

        # Count return indicators
        if any(keyword in line for keyword in CONTROL_FLOW_KEYWORDS["return"]["keywords"]):
            node_characteristics["return"] += 1

        # Count condition indicators
        if any(keyword in line for keyword in CONTROL_FLOW_KEYWORDS["condition"]["keywords"]) or any(
            op in line for op in CONTROL_FLOW_KEYWORDS["condition"]["operators"]
        ):
            node_characteristics["condition"] += 1

        # Count loop indicators
        if any(keyword in line for keyword in CONTROL_FLOW_KEYWORDS["loop"]["keywords"]) or any(
            pattern in line for pattern in CONTROL_FLOW_KEYWORDS["loop"]["patterns"]
        ):
            node_characteristics["loop"] += 1

        # Count function indicators
        if any(keyword in line for keyword in CONTROL_FLOW_KEYWORDS["function"]["keywords"]) or any(
            modifier in line for modifier in CONTROL_FLOW_KEYWORDS["function"]["modifiers"]
        ):
            node_characteristics["function"] += 1

        # Count error handling indicators
        if any(keyword in line for keyword in CONTROL_FLOW_KEYWORDS["error_handling"]["keywords"]) or any(
            pattern in line for pattern in CONTROL_FLOW_KEYWORDS["error_handling"]["patterns"]
        ):
            node_characteristics["error_handling"] += 1

    # Classify based on dominant characteristic
    # Priority: function > loop > condition > error_handling > assignment > return
    if node_characteristics["function"] > 0:
        return "function"
    elif node_characteristics["loop"] > 0:
        return "loop"
    elif node_characteristics["condition"] > 0:
        return "condition"
    elif node_characteristics["error_handling"] > 0:
        return "error_handling"
    elif node_characteristics["assignment"] > 0:
        return "assignment"
    elif node_characteristics["return"] > 0:
        return "return"

    return "other"


def classify_edge_type(edge_label):
    """Enhanced edge classification for multiple languages"""
    if not edge_label:
        return "sequential"

    label = edge_label.lower().strip()

    # True/false branches
    if any(word in label for word in ["true", "false", "yes", "no"]):
        return "condition"

    # Comparison operators
    if any(op in label for op in ["==", "!=", "<=", ">=", "<", ">", "===", "!=="]):
        return "condition"

    # Boolean expressions
    if any(expr in label for expr in ["&&", "||", "and", "or", "not", "!"]):
        return "condition"

    # Negation patterns
    if label.startswith("!(") or label.startswith("not "):
        return "condition"

    # Loop-related edges
    if any(word in label for word in ["continue", "break", "next", "iterate"]):
        return "loop"

    # Exception/error handling
    if any(word in label for word in ["exception", "error", "catch", "throw", "panic"]):
        return "exception"

    # Return edges
    if "return" in label:
        return "return"

    # Default sequential flow
    return "sequential"


def abstract_graph(nx_graph):
    node_types = {}
    for node, data in nx_graph.nodes(data=True):
        label = data.get("label", "").strip()
        node_type = get_node_type(label)
        node_types[node] = node_type

    abstracted_edges = set()
    for u, v, data in nx_graph.edges(data=True):
        u_type = node_types.get(u, "other")
        v_type = node_types.get(v, "other")
        edge_label = data.get("label", "").strip()
        branch_type = classify_edge_type(edge_label)

        abstracted_edges.add((u_type, branch_type, v_type))

    abstracted_nodes = set(node_types.values())
    return abstracted_nodes, abstracted_edges


def jaccard_similarity(setA, setB):
    intersection = len(setA & setB)
    union = len(setA | setB)
    return intersection / union if union else 1.0


def compute_cfg_similarity(cfg_file_1, cfg_file_2):
    """
    Compute CFG similarity with node, edge, and structural metrics

    Args:
        cfg_file_1, cfg_file_2: Parsed CFGs

    Returns:
        float: Overall similarity score (0-1)
    """

    dot_str1 = ""
    with open(cfg_file_1, "r") as f:
        dot_str1 = f.read()

    dot_str2 = ""
    with open(cfg_file_2, "r") as f:
        dot_str2 = f.read()

    cfg1 = parse_dot(dot_str1)
    cfg2 = parse_dot(dot_str2)

    nodes1, edges1 = abstract_graph(cfg1)
    nodes2, edges2 = abstract_graph(cfg2)

    # Calculate similarity metrics
    basic_node_sim = jaccard_similarity(nodes1, nodes2)
    basic_edge_sim = jaccard_similarity(edges1, edges2)

    # Weighted combination
    similarity_score = 0.5 * basic_node_sim + 0.5 * basic_edge_sim

    return similarity_score


if __name__ == "__main__":

    src_dot = ""
    with open("cfg_python", "r") as f:
        src_dot = f.read()

    trg_dot = ""
    with open("cfg_java", "r") as f:
        trg_dot = f.read()

    similarity = compute_cfg_similarity(src_dot, trg_dot)
    print(f"Similarity score between Python and Java DF Paths: {similarity:.4f}")
