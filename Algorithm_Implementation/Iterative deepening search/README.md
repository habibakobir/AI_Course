🧠 **Iterative Deepening Search (IDS) Algorithm**

🔹 **How the Algorithm Works:**
-Iterative Deepening Search (IDS) combines the advantages of both Depth-First Search (DFS) and Breadth-First Search (BFS).
It performs a series of Depth-Limited Searches (DLS) with increasing depth limits, starting from 0 up to the required level, until the goal is found.
It ensures completeness (like BFS) and low memory usage (like DFS).

**Steps:**

1.Start with depth limit = 0.
2.Perform Depth-Limited Search (DLS).
3.If the goal is not found, increase the depth limit by 1.
4.Repeat until the goal node is found or maximum depth is reached.

🔹**Applications of IDS:**

1.Used when depth of the solution is unknown.
2.Works well in large search spaces.
3.Commonly used in Artificial Intelligence, especially in state-space search problems (e.g., puzzles, games).
4.Helps avoid the memory limitations of BFS and the incompleteness of DFS.

🔹 **Time & Space Complexity:**
| Complexity Type | Value |
|------------------|--------|
| Time Complexity | O(b^d) — where b = branching factor, d = depth of the goal|
| Space Complexity | O(b × d) |

🔹 **Example Input & Output:**
A: [B, C]
B: [D]
C: [E]
D: [F]
E: [F]
F: []

Start Node: A
Goal Node: F
Maximum Depth: 4

🔹 **Output**
Goal found at depth 3 Path: A -> B -> D -> F
