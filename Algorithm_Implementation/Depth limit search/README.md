# 🧠 Depth-Limited Search (DLS) Algorithm

### 🔹 How the Algorithm Works
Depth-Limited Search (DLS) is a variation of the **Depth-First Search (DFS)** algorithm,  
where the search process is restricted to a **specific depth limit**.  
This means the algorithm explores nodes only up to a fixed level in the search tree.

It helps prevent infinite loops in large or infinite search spaces.

**Steps:**
1. Start from the root (source) node.  
2. Explore a branch using DFS until the depth limit is reached.  
3. If the goal is not found within the limit, backtrack.  
4. Continue exploring other branches within the same depth constraint.

### 🔹 Applications of DLS
- Used when the **depth of the solution is known**.  
- Prevents **infinite recursion** in large trees.  
- Commonly used in **AI search problems** and **game trees**.  
- Acts as a foundation for **Iterative Deepening Search (IDS)**.

### 🔹 Time & Space Complexity
| Complexity Type | Value |
|------------------|--------|
| Time Complexity | O(b^l) — where b = branching factor, l = depth limit |
| Space Complexity | O(b × l) |

### 🔹 Example Input & Output

**Example Graph (Simplified):**
A: [B, C]
B: [D, E]
C: [F]
D: []
E: [G]
F: []
G: []

**Depth Limit:** 2  
**Goal Node:** G  

**Search Process:**  
- Start at A → B → D (depth 2 reached, backtrack)  
- B → E (depth 2 reached, backtrack)  
- C → F (depth 2 reached, backtrack)  

**Result:** G not found (since G is at depth 3)
