"""Variable CFG path similarity utilities."""

from typing import Sequence, Any

import pydot
from types import SimpleNamespace

from .print_static_analysis import (
    DataFlowAnalyzer,
    parse_nodes_edges,
    build_pred_succ,
    remap_node_ids,
    get_variables_from_source,
)


def levenshtein_distance(seq1: Sequence[Any], seq2: Sequence[Any]) -> int:
    """Compute Levenshtein edit distance between two sequences."""
    m, n = len(seq1), len(seq2)
    if m == 0:
        return n
    if n == 0:
        return m
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if seq1[i - 1] == seq2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost  # deletion  # insertion  # substitution
            )
    return dp[m][n]


def levenshtein_similarity(seq1: Sequence[Any], seq2: Sequence[Any]) -> float:
    """Return normalized similarity score between 0 and 1."""
    max_len = max(len(seq1), len(seq2))
    if max_len == 0:
        return 1.0
    distance = levenshtein_distance(seq1, seq2)
    return 1 - distance / max_len


def jaccard_similarity(set1: set, set2: set) -> float:
    """Compute Jaccard similarity between two sets."""
    if not set1 and not set2:
        return 1.0
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union


def path_set_similarity(paths1, paths2):
    if not paths1 or not paths2:
        return 0.0

    def best_avg(source, target):
        total = 0.0
        for p1 in source:
            # best = max(levenshtein_similarity(p1, p2) for p2 in target)
            best = max(jaccard_similarity(set(p1), set(p2)) for p2 in target)
            total += best
        return total / len(source)

    sim1 = best_avg(paths1, paths2)
    sim2 = best_avg(paths2, paths1)
    return (sim1 + sim2) / 2


def compute_variable_cfg_similarity(paths_dict1, paths_dict2):
    """Compute similarity between two variable CFG path dictionaries."""
    if not paths_dict1 or not paths_dict2:
        return 0.0

    def best_scores(source, target):
        scores = []
        for var1, p1 in source.items():
            best = 0.0
            for var2, p2 in target.items():
                if len(p1) > 500 or len(p2) > 500:
                    # Skip long paths to avoid performance issues
                    continue
                sim = path_set_similarity(p1, p2)
                if sim > best:
                    best = sim
            scores.append(best)
        return sum(scores) / len(scores) if scores else 0.0

    sim_a = best_scores(paths_dict1, paths_dict2)
    sim_b = best_scores(paths_dict2, paths_dict1)
    return (sim_a + sim_b) / 2


def _extract_paths_for_graph(graph, variables):
    nodes, edges = parse_nodes_edges(graph)
    if not nodes:
        return {}
    preds, succs = build_pred_succ(nodes, edges)
    parameters = variables.get("parameters", []) if variables else []
    all_vars = []
    if variables:
        all_vars.extend(variables.get("local_vars", []))
        all_vars.extend(variables.get("parameters", []))
    mapping, entry_orig = remap_node_ids(nodes, preds, parameters)
    remapped_succs = {}
    for orig_node, succ_list in succs.items():
        remapped_succs[mapping[orig_node]] = [(mapping[dst], label) for dst, label in succ_list]
    if parameters and entry_orig:
        remapped_succs[0] = [(1, "")]
        remapped_succs[1] = [(mapping[e], "") for e in entry_orig]
    analyzer = DataFlowAnalyzer()
    analyzer.analyze_variable_usage(nodes, all_vars, mapping, parameters)
    raw_paths = analyzer.extract_dataflow_paths(all_vars, remapped_succs)
    result = {}
    for var, plist in raw_paths.items():
        result[var] = [p["path"] for p in plist]
    return result


def get_variable_paths(dot_file, source_file, language):
    """Extract variable CFG paths from a dot/source pair."""
    args = SimpleNamespace(source_file=source_file, language=language)
    variables = get_variables_from_source(args)
    with open(dot_file, "r") as f:
        dot_data = f.read()
    graphs = pydot.graph_from_dot_data(dot_data)
    if not graphs:
        return {}
    top = graphs[0]
    paths = {}
    subs = top.get_subgraphs()
    if subs:
        for sub in subs:
            sub_paths = _extract_paths_for_graph(sub, variables)
            for var, plist in sub_paths.items():
                paths.setdefault(var, []).extend(plist)
    else:
        paths.update(_extract_paths_for_graph(top, variables))
    return paths


def compute_variable_cfg_similarity_from_files(dot1, src1, lang1, dot2, src2, lang2):
    paths1 = get_variable_paths(dot1, src1, lang1)
    paths2 = get_variable_paths(dot2, src2, lang2)
    try:
        return compute_variable_cfg_similarity(paths1, paths2)
    except Exception as e:
        print(f"Error computing similarity: {e}")
        return 0.0


if __name__ == "__main__":
    # Example usage
    dot_file1 = "cfg_c"
    src_file1 = "snippet_c"
    lang1 = "c"

    dot_file2 = "cfg_python"
    src_file2 = "snippet_python"
    lang2 = "python"

    similarity_score = compute_variable_cfg_similarity_from_files(
        dot_file1, src_file1, lang1, dot_file2, src_file2, lang2
    )
    print(f"Variable CFG similarity score: {similarity_score:.4f}")
