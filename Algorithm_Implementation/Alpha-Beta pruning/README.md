# 🧠 Alpha-Beta Pruning Algorithm

### 🔹 How the Algorithm Works
Alpha-Beta Pruning is an **optimization of the Minimax algorithm** used in game trees.  
It reduces the number of nodes evaluated by the Minimax algorithm without affecting the final result.  

- **Alpha (α):** Best already explored option along the path to the **maximizer**.  
- **Beta (β):** Best already explored option along the path to the **minimizer**.  

**Steps:**
1. Start from the root node of the game tree.  
2. Traverse the tree using Minimax logic:  
   - For **maximizer nodes**, update α.  
   - For **minimizer nodes**, update β.  
3. **Prune** branches where the current node cannot improve the outcome:  
   - If `α >= β`, prune the remaining branches.  
4. Continue until all nodes are evaluated or pruned, and return the optimal move.  

---

### 🔹 Applications of Alpha-Beta Pruning
- **Two-player games** like Chess, Tic-Tac-Toe, Checkers.  
- Reduces computation in **game AI**.  
- Works as an optimization over the standard **Minimax algorithm**.  

---

### 🔹 Time & Space Complexity
| Complexity Type | Value |
|-----------------|-------|
| Time Complexity  | O(b^(m/2)) in best case (b = branching factor, m = depth) |
| Space Complexity | O(m) (recursive stack depth) |

---

### 🔹 Example Game Tree
        A (MAX)
       /       \
     B (MIN)    C (MIN)
    /           \
   D (MAX)       E (MAX)
  \             \
  F (leaf)      F (leaf)


Root node:A(MAX)
Leaf node values: F
Number of nodes: 6
Nodes and children:
   tree = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["F"],
    "F": []
}
# Leaf node utility values
leaf_values = {
    "F": 10  # Example value for leaf F
}

Optimal value at root 'A': 10
Decision path: A → B → D → F(10)
Total prunings: 2
Pruned nodes: None
Optimal value for MAX: 10
Maximizer tries to get highest value, Minimizer tries lowest value
