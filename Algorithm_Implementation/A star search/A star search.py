# Step 1: Build the graph with costs and heuristics
graph = {}
costs = {}
heuristic = {}

n = int(input("Number of nodes: "))
for i in range(n):
    node = input(f"Node name {i+1}: ")
    neighbors = input(f"Neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

    for neighbor in neighbors:
        edge_cost = int(input(f"Cost from {node} to {neighbor}: "))
        costs[(node, neighbor)] = edge_cost

    h = int(input(f"Heuristic value for {node}: "))
    heuristic[node] = h

# Step 2: A* Search function
def a_star(start, goal):
    open_set = {start}
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]

    while open_set:
        current = min(open_set, key=lambda x: f_score[x])
        print(f"Visiting: {current}")
        
        if current == goal:
            print("\nGoal reached!")
            reconstruct_path(came_from, current)
            return

        open_set.remove(current)

        for neighbor in graph[current]:
            tentative_g = g_score[current] + costs[(current, neighbor)]
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic[neighbor]
                open_set.add(neighbor)

    print("\nGoal not reachable.")

# Step 3: Path reconstruction
def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    print("Path:", " -> ".join(path))

# Step 4: Run the search
start = input("Start node: ")
goal = input("Goal node: ")
a_star(start, goal)
