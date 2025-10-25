# ♟️ Chess (Human vs AI)

## 🧭 Project Overview
This project is an **Artificial Intelligence-based Chess Game** built with **Python** and **Pygame / Chess library**.  
It allows a human player to play against a computer-controlled opponent powered by an AI algorithm such as **Minimax with Alpha-Beta Pruning**.  

The AI analyzes all possible future moves and selects the one that maximizes its winning chances while minimizing the opponent’s advantage.

---

## ⚙️ How to Run

### 🧩 Step 1: Install Python
Make sure Python 3.8 or above is installed.  
You can check your version using:
```bash
python --version

### 🧩 Step 2: Install Required Libraries

**Install these libraries:**

pip install pygame

pip install python-chess

### 🧩 Step 3: Run the Game

Navigate to the Chess folder and run the main file:

python Chess.py

**💡 How to Play:**

1.The player always uses White pieces (moves first).

2.The AI plays as Black pieces.

3.Use your mouse to click and move pieces following normal chess rules.

4.The AI will automatically make its move after you.

5.The game ends when a Checkmate, Draw, or Stalemate occurs.

**🧠 Algorithm Used:**

**🧩 Minimax Algorithm with Alpha-Beta Pruning**

1.The Minimax Algorithm is used for decision-making in two-player games.

2.It recursively explores all possible moves to determine the best one.

3.Alpha-Beta Pruning is applied to reduce the number of nodes evaluated by the Minimax algorithm, making the AI faster and more efficient.

### 🧱 Libraries / Frameworks Used:

**Library	Purpose**

Python	Programming language

Pygame	GUI and board display

python-chess	Handling chess logic and moves


**🏆 Summary**

This project demonstrates how Artificial Intelligence can be used to simulate intelligent gameplay in a complex strategy game like Chess.
Using the Minimax Algorithm with Alpha-Beta Pruning, the AI can efficiently choose strong moves and challenge the human player.
