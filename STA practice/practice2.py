nodes = {}

with open("data.txt", "r") as f:
    lines = f.readlines() #Reads all lines from the file n Stores them in a list

for line in lines:
    line = line.strip() #Removes extra spaces and newline (\n)
    name, delay = line.split() #Splits a string by spaces,separate node name and its delay.
    nodes[name] = int(delay) #convert delay from string to int,and assign key-values to dict

print("Nodes read from file:")
for name in nodes:
    print(name, "->", nodes[name])
