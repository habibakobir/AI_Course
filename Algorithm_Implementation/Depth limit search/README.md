# 🧩 Depth-First Search (DFS) Algorithm

### 🔹 How the Algorithm Works
Depth-First Search (DFS) is a graph traversal algorithm that explores as far as possible along one branch before backtracking.  
It uses a **stack** data structure (either explicitly or via recursion) to remember which nodes to visit next.

**Steps:**
1. Start from the source (root) node.  
2. Visit the node and mark it as visited.  
3. Recursively explore each unvisited neighbor.  
4. Backtrack when no unvisited neighbors are left.  

### 🔹 Applications of DFS
- **Pathfinding** and **maze solving**  
- **Topological sorting**  
- **Cycle detection** in graphs  
- **Solving puzzles** like Sudoku or N-Queens  
- **Connected components** detection in a graph  

### 🔹 Time & Space Complexity
| Complexity Type | Value |
|------------------|--------|
| Time Complexity | O(V + E) — where V = vertices, E = edges |
| Space Complexity | O(V) (for recursion stack) |

### 🔹 Example Input & Output

**Input Graph (Adjacency List):**

A: [B, C]
B: [D, E]
C: [F]
D: []
E: [F]
F: []

**DFS Traversal:**  
A → B → D → E → F → C
