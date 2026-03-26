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