# EduSTA - Educational Static Timing Analysis Tool

# computing Tcomb
def compute_Tcomb(path, delays):
    Tcomb = 0
    for i in range(len(path) - 1):  # len(path) = 4 for below example
        start = path[i]
        end = path[i + 1]
        Tcomb = Tcomb + delays[(start, end)]
    return Tcomb

# Setup time check
def check_setup(Tclk, Tcq, Tcomb, Tsetup):
    setup_slack = Tclk - (Tcq + Tcomb + Tsetup)
    return setup_slack

# Hold time check
def check_hold(Tcq_min, Tcomb_min, Thold):
    hold_slack = (Tcq_min + Tcomb_min) - Thold
    return hold_slack

# Build timing graph from edges
def build_graph(edges):
    graph = {}
    delays = {}

    for src, dst, delay in edges:
        if src not in graph:
            graph[src] = []
        graph[src].append(dst)
        delays[(src, dst)] = delay

    return graph, delays

# Find all paths using DFS
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
            new_paths = find_all_paths(graph, node, end, path)
            paths.extend(new_paths)

    return paths

                                   # Example usage (single-path STA)
# Run this file directly to see example STA calculations

if __name__ == "__main__":
#Run the code below only if this file is executed directly, NOT if it is imported by another file.”

    # timing path (order of data flow)
    path = ["FF1", "G1", "G2", "FF2"]  # Order matters in a timing path, so we use a LIST not dict
    print("Timing path:")
    for block in path:
        print(block)

    # delays between blocks (in ns)
    delays = {  # used a DICT to map (start_block, end_block) [tuple used] -> delay
        ("FF1", "G1"): 1.5,
        ("G1", "G2"): 2.0,
        ("G2", "FF2"): 3.0
    }

    Tcomb = compute_Tcomb(path, delays)
    print("Total combinational delay =", Tcomb, "ns")

    # Setup time parameters
    Tclk = 10.0    # clock period
    Tcq = 1.0      # clock-to-Q
    Tsetup = 2.5   # setup time

    setup_slack = check_setup(Tclk, Tcq, Tcomb, Tsetup)
    print("Setup slack =", setup_slack, "ns")

    if setup_slack >= 0:
        print("SETUP CHECK: PASS")
    else:
        print("SETUP CHECK: FAIL(Setup violation)")

    # Hold time parameters
    Tcq_min = 0.5   # minimum clock-to-Q delay
    Thold = 1.0     # hold time

    # For now, assume minimum combinational delay = Tcomb
    Tcomb_min = Tcomb

    hold_slack = check_hold(Tcq_min, Tcomb_min, Thold)
    print("Hold slack =", hold_slack, "ns")

    if hold_slack >= 0:
        print("HOLD CHECK: PASS")
    else:
        print("HOLD CHECK: FAIL(hold violation)")
