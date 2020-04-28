# 2x2x2-Rubiks-Cube-Solver
Using Breadth First Search to determine the optimal solution for a 2x2x2 Rubik's Cube

## Usage
* **Run the bfs.py script.** This will create 2 new files in the same directory which will be used to later solve the Rubik's cube. This script is responsible for exploring the **graph** where each **node** of the graph represents one of the 264 million states that the 2x2x2 Rubik's cube could be in. The **edges** of the graph represent a move; for a 2x2x2 Rubik's cube the possible moves are: **F, Fi, F2, L, Li, L2, U, Ui, U2** (these are standard). The letters F, U, L represent the face that the move is being performed on, F=Front, U=Up, L=Left while the indeces i represent a twist in the counter-clockwise direction, and 2 represents a double twist. Therefore the BFS algorithm starts from the "solved state" (represented with an I for identity) and visits every possible state by performing all valid moves from the current state.

* **Input the scrambled state in the Rubik.py script.** Each face is represented as a 2x2 matrix. Orient the Rubik's Cube such that the cubie with colors **yellow, blue, orange** is in the **bottom, right, back** position with the yellow face of the cubie facing down. Next input the colors of the six faces.

* **Finally run the solver.py script.** This script will output a sequence of moves to solve Rubik's Cube. The maximum number of moves to solve any of the 264 million states is 11, which is also known as the God's Number for a 2x2x2 Rubik's cube and because of the BFS algorithm we can be certain that it outputs the optimal solution! 
