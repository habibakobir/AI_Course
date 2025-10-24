from collections import deque

# BFS Function
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])

# ----- User Input -----
graph = {}
n = int(input("Number of nodes: "))
for i in range(n):
    node = input(f"Node name {i+1}: ")
    graph[node] = input(f"Neighbors of {node} (space separated): ").split()

start = input("Start node: ")
print("BFS Traversal:")
bfs(graph, start)
