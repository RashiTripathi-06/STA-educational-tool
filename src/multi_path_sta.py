 #Multi-path STA using a simple engine

from sta_engine import compute_Tcomb, check_setup, check_hold
from circuit_models import example_multi_path_circuit

def build_graph(edges):
    graph = {} #(dict to show connection)
    delays = {} #(dict to show delays between nodes)

    for src, dst, delay in edges:
        if src not in graph:
            graph[src] = []     #If it is the first time, we see src(eg-FF1),create an empty list
        graph[src].append(dst)  #Add a directed connection
        delays[(src,dst)] = delay  #tuple (src, dst) is used as a key, value is delay

    return graph, delays

"""
graph = {
    "FF1": ["G1"],
    "G1": ["G2", "FF3"],
    "FF3": ["G2"],
    "G2": ["FF2"]
}
 
delays = {
    ("FF1", "G1"): 1.5,
    ("G1", "G2"): 2.0,
    ("G2", "FF2"): 3.0,
    ("G1", "FF3"): 1.0,
    ("FF3", "G2"): 0.8
}
"""

# using DFS to find all paths
def find_all_paths(graph, start, end, path=None):
    if path is None: 
        path = [] # when used for the first time, intialize path as empty list

    path = path + [start] # we add path so far + current node

    if start == end:
        return [path] 
    """ 
    as DFS runs, start keeps changing, so like initially start=FF1, next G1, next G2, next FF2
    find_all_paths(graph, "G2", "FF2", ["FF1","G1"]), then
    find_all_paths(graph, "FF2", "FF2", ["FF1","G1","G2"])
       now start == end == "FF2", so we return [path] which is [["FF1","G1","G2","FF2"]] """


    if start not in graph:
        return []
    #If start is not the destination, and start has no outgoing edges, it means no path exists, so return empty list

    paths = []
    for node in graph[start]:
        if node not in path:
            paths.extend(find_all_paths(graph, node, end,    path))

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
        print("Path:", " -> ".join(path)) #.join is used to convert list to string with separator " -> "

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

    print("STA SUMMARY")
    print("Critical Path:")
    print(" -> ".join(critical_path))
    print(f"Worst Setup Slack = {worst_setup_slack:.2f} ns")
