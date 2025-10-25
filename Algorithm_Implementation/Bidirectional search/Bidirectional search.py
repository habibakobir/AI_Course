from collections import deque

# Function for one step BFS
def bfs_step(graph, queue, visited, other_visited):
    if queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited[neighbor] = node
                queue.append(neighbor)
                if neighbor in other_visited:
                    return neighbor
    return None

# Function to reconstruct path from start to goal
def construct_path(meeting_node, visited_start, visited_goal):
    # From start side
    path_start = []
    node = meeting_node
    while node is not None:
        path_start.append(node)
        node = visited_start[node]
    path_start.reverse()

    # From goal side
    path_goal = []
    node = visited_goal[meeting_node]
    while node is not None:
        path_goal.append(node)
        node = visited_goal[node]

    return path_start + path_goal

# Main bidirectional search
def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    # Initialize BFS from both sides
    queue_start = deque([start])
    queue_goal = deque([goal])

    visited_start = {start: None}
    visited_goal = {goal: None}

    while queue_start and queue_goal:
        # Expand from start side
        meet_node = bfs_step(graph, queue_start, visited_start, visited_goal)
        if meet_node:
            return construct_path(meet_node, visited_start, visited_goal)

        # Expand from goal side
        meet_node = bfs_step(graph, queue_goal, visited_goal, visited_start)
        if meet_node:
            return construct_path(meet_node, visited_start, visited_goal)

    return None


# ------------------ USER INPUT ------------------

graph = {}
n = int(input("Enter number of nodes: "))
for i in range(n):
    node = input(f"Enter node {i+1} name: ")
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

start = input("Enter start node: ")
goal = input("Enter goal node: ")

result = bidirectional_search(graph, start, goal)

if result:
    print("Path found:", " -> ".join(result))
else:
    print("No path found between", start, "and", goal)