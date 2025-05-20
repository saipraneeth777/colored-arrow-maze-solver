# 🎯 Colored Arrow Maze Solver

![Python](https://img.shields.io/badge/Python-3.13%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Solve mazes of colored arrows using graph traversal! This project finds a path from the top-left to the bullseye in the bottom-right, following alternating color rules. It features a text-based maze visualizer, performance stats, and a random maze generator for endless fun.

---

## 🚀 Features
- **Maze Solver**: Finds a valid path through colored arrow mazes.
- **Text-Based Visualizer**: See the solution path in your terminal, marked with `*`.
- **Performance Stats**: See how many nodes were visited and how fast the maze was solved.
- **Random Maze Generator**: Instantly create new mazes to challenge the solver!

---

## 🛠️ How to Run

1. **Solve a Maze**
   ```bash
   python Project2.py input.txt output.txt
   ```
   - `input.txt`: Your maze file (see format below)
   - `output.txt`: Solution path will be written here

2. **Generate a Random Maze**
   ```bash
   python random_maze_generator.py 8 8 random_maze.txt
   ```
   - This creates an 8x8 random maze in `random_maze.txt`.

---

## 📥 Input Example
```
3 4
B-S R-E B-SE B-SW
R-E B-E R-S R-S
R-N R-NE B-N O
```

## 📤 Output Example
```
1S 1E 2E 1S
```

---

## 🖼️ Screenshot

```
Maze with solution path ('*' marks the path):
* R-E B-SE B-SW
* * R-S *
R-N R-NE B-N O

Performance stats:
Nodes visited: 6
Time taken: 0.000010 seconds
```

---

## 📦 Requirements
- Python 3.13+

---

## 👤 Credits
- Developed for COT 6405 (Fall 2021)
- Your Name

---

## 📄 License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details. 