 #Educational multi-path STA using a simple engine
from sta_engine import compute_Tcomb, check_setup, check_hold
from circuit_models import example_multi_path_circuit

# Build graph from edges
def build_graph(edges):
    graph = {}
    delays = {}

    for src, dst, delay in edges:
        if src not in graph:
            graph[src] = []
        graph[src].append(dst)
        delays[(src,dst)] = delay

    return graph, delays


# DFS to find all paths
def find_all_paths(graph, start, end, path=None):
    if path is None:
        path = []

    path = path + [start]

    if start == end:
        return [path]

    if start not in graph:
        return []

    paths = []
    for node in graph[start]:
        if node not in path:
            paths.extend(find_all_paths(graph, node, end, path))

    return paths

# Main STA Flow
if __name__ == "__main__":

    # Load circuit
    edges, launch_ff, capture_ff = example_multi_path_circuit()
    graph, delays = build_graph(edges)

    # Timing parameters
    Tclk = 10.0
    Tcq = 1.0
    Tsetup = 2.5
    Tcq_min = 0.5
    Thold = 1.0

    paths = find_all_paths(graph, launch_ff, capture_ff)

    print("\n=== Running Multi-Path STA ===\n")

    worst_setup_slack = float("inf")
    critical_path = None

    for path in paths:
        print("Path:", " -> ".join(path))

        Tcomb = compute_Tcomb(path, delays)

        setup_slack = check_setup(Tclk, Tcq, Tcomb, Tsetup)
        hold_slack = check_hold(Tcq_min, Tcomb, Thold)

        print(f"  Tcomb       = {Tcomb:.2f} ns")
        print(f"  Setup slack = {setup_slack:.2f} ns")
        print(f"  Hold slack  = {hold_slack:.2f} ns")

        if setup_slack < worst_setup_slack:
            worst_setup_slack = setup_slack
            critical_path = path

        if setup_slack < 0:
            print("Setup violation")

        if hold_slack < 0:
            print("Hold violation")

        print()

    print("=== STA SUMMARY ===")
    print("Critical Path:")
    print(" -> ".join(critical_path))
    print(f"Worst Setup Slack = {worst_setup_slack:.2f} ns")
