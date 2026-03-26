# EduSTA - Educational Static Timing Analysis Tool

# computing Tcomb
def compute_Tcomb(path, delays):
    Tcomb = 0
    for i in range(len(path) - 1):  # len(path) = 4 for single path example
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
    graph = {} #(dict to show connection)
    delays = {} #(dict to show delays between nodes)

    for src, dst, delay in edges:
        if src not in graph:
            graph[src] = []     #If it is the first time, we see src(eg-FF1),create an empty list
        graph[src].append(dst)  #Add a directed connection
        delays[(src,dst)] = delay  #tuple (src, dst) is used as a key, value is delay

    return graph, delays



