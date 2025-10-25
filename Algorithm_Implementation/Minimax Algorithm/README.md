# 🧠 Minimax Algorithm

### 🔹 How the Algorithm Works
Minimax is a **decision-making algorithm** used in **two-player zero-sum games**.  
It assumes that both players play optimally:

- **MAX player** tries to **maximize** the score.  
- **MIN player** tries to **minimize** the score.  

The algorithm recursively explores all possible moves to determine the **optimal move** for the current player.  

**Steps:**
1. Start from the root node (current game state).  
2. Recursively evaluate all possible moves:  
   - MAX node → choose the **maximum value** among child nodes.  
   - MIN node → choose the **minimum value** among child nodes.  
3. Leaf nodes contain the utility (score) of the game state.  
4. Backpropagate values to determine the optimal move at the root.  

---

### 🔹 Applications of Minimax
- Two-player games like **Tic-Tac-Toe, Chess, Checkers**  
- Game AI to select **optimal moves**  
- Base algorithm for **Alpha-Beta pruning** optimization  

---

### 🔹 Time & Space Complexity
| Complexity Type | Value |
|-----------------|-------|
| Time Complexity  | O(b^m) — where b = branching factor, m = max depth |
| Space Complexity | O(m) — recursive call stack |

---

### 🔹 Example Game Tree
         A (MAX)
       /       \
     B (MIN)    C (MIN)
    /           \
   D (MAX)       E (MAX)
    \             \
     F1 (leaf)     F2 (leaf)

# Game tree adjacency list:

tree = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["F"],
    "F1": [],
    "F2":[],
}

Leaf node values example: F1 =3 ,F = 5 ,
Root node: A (MAX) chooses path leading to highest leaf value → F2 = 5 ,

Decision path: A → C → E → F2
Optimal value for MAX: 5 ,
Decision path: A → B → D → F2 ,
MAX tries to maximize the value, MIN tries to minimize

