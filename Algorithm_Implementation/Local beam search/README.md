# 🧠 Beam Search Algorithm

### 🔹 How the Algorithm Works
Beam Search is a **heuristic search algorithm** similar to Breadth-First Search (BFS),  
but it processes **only a fixed number of the most promising nodes** at each level.  
This number is called the **beam width**.  

Beam Search is memory-efficient and faster, but it does not always guarantee the optimal solution.  

**Steps:**
1. Start from the root (source) node.  
2. Expand all children of the current nodes.  
3. Keep only the top `beam width` nodes based on a heuristic evaluation.  
4. Repeat until the goal node is found or no nodes are left to explore.  

### 🔹 Applications of Beam Search
- Used in **AI search problems** with memory constraints.  
- Common in **Natural Language Processing** (e.g., machine translation, text generation).  
- Useful in **pathfinding** where full BFS/DFS is too expensive.  
- Acts as a faster, memory-efficient alternative to BFS.  

### 🔹 Time & Space Complexity
| Complexity Type | Value |
|-----------------|-------|
| Time Complexity  | O(b × k × d) — where b = branching factor, k = beam width, d = depth of search |
| Space Complexity | O(k × d) | 

### 🔹 Example Input & Output

**Example Graph (Simplified):**  
Graph:
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["F"],
    "F": []

heuristic = {
    "A": 3,
    "B": 2,
    "C": 2,
    "D": 1,
    "E": 1,
    "F": 0
}

Start: A
Goal: F
Beam width: 2

**Output:** 
Path found: A → C → E → F
