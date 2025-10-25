# 🧠 Greedy Best-First Search Algorithm

### 🔹 How the Algorithm Works
Greedy Best-First Search is a **heuristic search algorithm** that selects the node which appears to be **closest to the goal** according to a heuristic function `h(n)`.  

It does **not consider the cost from the start node** (`g(n)`), unlike A*, so it is faster but may not always find the optimal path.  

**Steps:**
1. Initialize the open list with the start node.  
2. Repeat until the goal is found or open list is empty:  
   - Select the node with the lowest heuristic value `h(n)` from the open list.  
   - If node is the goal, return the path.  
   - Expand the node's neighbors and add them to the open list.  
3. Continue until the goal node is reached.  

---

### 🔹 Applications of Greedy Best-First Search
- Pathfinding in **games**  
- **Robot navigation** for faster solutions  
- **AI search problems** where speed is preferred over optimality  

---

### 🔹 Time & Space Complexity
| Complexity Type | Value |
|-----------------|-------|
| Time Complexity  | O(b^m) — worst case (b = branching factor, m = max depth) |
| Space Complexity | O(b^m) (stores all generated nodes) |

---

### 🔹 Example Graph
**Graph (Adjacency List):**  
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["F"],
    "F": []
}

**Heuristic values (h(n)) for Greedy Best-First Search:**
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
