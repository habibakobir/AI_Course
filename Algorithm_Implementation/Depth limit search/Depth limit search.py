#Function define
def dls(graph, start, goal, limit, path=None):
    
    #Path initialize    
    if path is None:
        path = []

    path.append(start)

    #if goal found
    if start == goal:
        return path

    #limit check
    if limit <= 0:
        path.pop()
        return None

    #neighbor nodes check
    if start in graph:
        for neighbor in graph[start]:
            if neighbor not in path:
                result = dls(graph, neighbor, goal, limit - 1, path)
                if result is not None:
                    return result
    #backtracking
    path.pop()
    return None


# ----------- User Input -----------
graph = {}
n = int(input("Enter number of nodes: "))

# Graph input 
for i in range(n):
    node = input(f"Enter node {i+1}: ")
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    graph[node] = neighbors
    
#node input
start = input("Enter start node: ")
goal = input("Enter goal node: ")
limit = int(input("Enter depth limit: "))

#result check
result = dls(graph, start, goal, limit)

if result:
    print("Goal found! Path:", " -> ".join(result))
else:

    print("Goal not found within depth limit.")
