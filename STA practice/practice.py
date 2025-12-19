nodes = { #The points where timing is measured are called nodes
    "FF1": 0, #FF1 is the starting point of data. When the clock edge happens: FF1 launches data
    "G1": 2,
    "G2": 3
}

print("Printing nodes and delays:")
for name in nodes:
    print(name, "->", nodes[name])
    