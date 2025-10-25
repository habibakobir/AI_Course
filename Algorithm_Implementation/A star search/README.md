# 🧠 A* (A-Star) Search Algorithm

### 🔹 How the Algorithm Works
A* Search is a **best-first search algorithm** that finds the **shortest path** from a start node to a goal node using:  
f(n) = g(n) + h(n)

- `g(n)` = cost from start node to current node `n`  
- `h(n)` = heuristic estimate of cost from `n` to goal  

It selects the node with the lowest `f(n)` at each step, combining both actual cost and estimated cost to reach the goal.  

**Steps:**
1. Initialize open list with the start node.  
2. Repeat until the goal is found or open list is empty:  
   - Select the node with the lowest `f(n)` from open list.  
   - If node is goal, return path.  
   - Expand neighbors, calculate `f(n)` for each, and add to open list if not visited.  
3. Backtrack to get the optimal path.  

---

### 🔹 Applications of A*
- Pathfinding in **games** and **robotics**  
- GPS navigation systems  
- AI **search problems** requiring optimal paths  
- Graph traversal where cost matters  

---

### 🔹 Time & Space Complexity
| Complexity Type | Value |
|-----------------|-------|
| Time Complexity  | O(b^d) in worst case (b = branching factor, d = depth) |
| Space Complexity | O(b^d) (stores all generated nodes) |

---

### 🔹 Example Graph
**Graph (Adjacency List with costs):**  
graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("D", 2)],
    "C": [("E", 5)],
    "D": [("F", 1)],
    "E": [("F", 2)],
    "F": []
}
**Heuristic values (h(n)) for A:**

heuristic = {
    "A": 6,
    "B": 4,
    "C": 4,
    "D": 2,
    "E": 2,
    "F": 0
}

🔹 **Input & Output Example:**

Start node: A
Goal node: F

**Output:**

Path found: A → B → D → F

