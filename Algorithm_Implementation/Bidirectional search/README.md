
# 🔄 Bidirectional Search Algorithm

### 🔹 How the Algorithm Works
Bidirectional Search is an optimization of Breadth-First Search (BFS).  
It simultaneously searches **forward from the start node** and **backward from the goal node** until the two searches meet in the middle.  
This approach reduces the time complexity significantly compared to traditional BFS.

**Steps:**
1. Initialize two queues — one starting from the **source** and one from the **destination**.  
2. Perform BFS from both sides alternately.  
3. When a node is found that is common to both searches, the path is found.  
4. Merge the two paths to form the final shortest route.

---

### 🔹 Applications of Bidirectional Search
- **Shortest path search** in large graphs (e.g., maps, networks).  
- **Route finding** in GPS navigation systems.  
- **Social networks** (finding mutual connections).  
- **AI-based games** (path optimization).  

---

### 🔹 Time & Space Complexity
| Complexity Type | Value |
|------------------|--------|
| Time Complexity | O(b^(d/2)) — where b = branching factor, d = distance between nodes |
| Space Complexity | O(b^(d/2)) |

*(It’s faster than BFS when both start and goal nodes are known.)*

---

### 🔹 Example Input & Output

**Input Graph (Simplified):**
A: [B, C]
B: [D]
C: [E]
D: [F]
E: [F]
F: []

**Start Node:** A  
**Goal Node:** F  

**Search Process:**  
- Forward from A → A, B, C  
- Backward from F → F, D, E  
- Meeting point → F  

**Result:** Path found: A → B → D → F
