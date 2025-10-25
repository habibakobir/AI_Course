# Step 1: Build the graph and heuristic
graph = {}
heuristic = {}

n = int(input("Number of nodes: "))
for i in range(n):
    node = input(f"Node name {i+1}: ")
    graph[node] = input(f"Neighbors of {node} (space separated): ").split()
    h = int(input(f"Heuristic value for {node}: "))
    heuristic[node] = h

# Step 2: Beam Search function
def beam_search(start, goal, beam_width):
    visited = set()
    queue = [start]

    while queue:
        print("Current Beam:", queue)
        next_level = []

        for node in queue:
            if node == goal:
                print(f"\nGoal '{goal}' reached!")
                return
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    next_level.append(neighbor)

        # Sort next level by heuristic and keep top-k (beam width)
        next_level.sort(key=lambda x: heuristic[x])
        queue = next_level[:beam_width]

    print("\nGoal not reachable.")

# Step 3: Run the search
start = input("Start node: ")
goal = input("Goal node: ")
beam_width = int(input("Beam width (k): "))
beam_search(start, goal, beam_width)
