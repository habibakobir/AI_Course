def dls(graph, start, goal, limit, path):
    #if goal found
    if start == goal:
        return path
    
    if limit <= 0:
        return None
    
    if start not in graph:
        return None

    for neighbor in graph[start]:
        if neighbor not in path:  
            result = dls(graph, neighbor, goal, limit - 1, path + [neighbor])
            if result is not None:
                return result
    return None


def ids(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"Searching at depth limit = {depth}")
        result = dls(graph, start, goal, depth, [start])
        if result is not None:
            return result
    return None


# --------- User Input ----------
graph = {}
n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input(f"Enter node {i+1} name: ")
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

start = input("Enter start node: ")
goal = input("Enter goal node: ")
max_depth = int(input("Enter maximum depth limit: "))

result = ids(graph, start, goal, max_depth)

if result:
    print("Goal found! Path:", " -> ".join(result))
else:
    print("Goal not found within depth limit.")