
# 🔹Breadth-First Search (BFS) Algorithm

### 🔹How the Algorithm Works
Breadth-First Search (BFS) is a graph traversal algorithm that explores all nodes at the present depth level before moving on to the nodes at the next depth level.  
It uses a **queue** data structure to keep track of nodes to visit next.

**Steps:**
1. Start from the source node.  
2. Visit all its immediate neighbors (children).  
3. Add unvisited neighbors to the queue.  
4. Dequeue the next node and repeat the process until all nodes are visited or the goal is found.

### 🔹 Applications of BFS
- Finding the **shortest path** in unweighted graphs  
- **Web crawling** and network broadcasting  
- **Social network** connection analysis (finding degrees of separation)  
- **AI pathfinding** in games or maps  

### 🔹 Time & Space Complexity
| Complexity Type | Value |
|------------------|--------|
| Time Complexity | O(V + E) — where V = vertices, E = edges |
| Space Complexity | O(V) |

### 🔹 Example Input & Output

**Input Graph (Adjacency List):**
A: [B, C]
B: [D, E]
C: [F]
D: []
E: [F]
F: []
**Output (BFS Traversal):**
A, B, C, D, E, F
