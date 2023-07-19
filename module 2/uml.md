```
+------------------------------------+
|          <<abstract>>              |
|           Algorithm                |
+------------------------------------+
| - boardGame: Board                 |
+-------------------------------------------------+
| + bestMove(boardGame: Board, letter: char): int |
+-------------------------------------------------+

+-------------------------------+
|         <<abstract>>          |
|            Board              |
+-------------------------------+
| - dimension: int              |
+--------------------------------------------------+
| + createBoard(): void                            |
| + printBoard(): void                             |
| + setCellState(position: int, state: char): void |
| + getCellState(position: int): char              |
| + getBoardState(): dict                          |
| + getBoardDimensions(): int                      |
+--------------------------------------------------+

+----------------------------------+
|          <<abstract>>            |
|           GameLogic              |
+----------------------------------+
| - boardGame: Board               |
+---------------------------------------------------+
| + chkForWin(): bool                               |
| + chkForDraw(): bool                              |
| + chkMarkForWin(letter: char): bool               |
| + insertLetter(letter: char, position: int): void |
| + spaceIsFree(position: int): bool                |
+---------------------------------------------------+

+-------------------------------+
|        <<abstract>>           |
|           Player              |
+-------------------------------+
| - letter: char                |
| - algorithm: Algorithm        |
+-----------------------------------------------+
| + chooseAlgorithm(algorithm: Algorithm): void |
| + makeMove(board: Board): void                |
+-----------------------------------------------+
```

- **GameLogic** is an abstract class that defines the game logic. It has a **Board** object as a member variable. It also has methods to check for a win, check for a draw, check for a win for a specific letter, insert a letter in a specific position, and check if a space is free.
- **GameLogic** has a dependency with **Board**.
- **GameLogic** is open for extension because it can be extended to support different games.
- **GameLogic** is closed for modification because it does not need to be modified to support different games.
---
- **Board** is an abstract class that defines the board. It has a **Board** object as a member variable. It also has methods to create the board, print the board, set the state of a cell, get the state of a cell, get the state of the board, and get the dimensions of the board.
- **Board** has no dependencies.
- **Board** is open for extension because it can be extended to support different boards.
- **Board** is closed for modification because it does not need to be modified to support different boards.
---
- **Player** is an abstract class that defines the player. It has a letter and an algorithm as member variables. It also has methods to choose an algorithm and make a move.
- **Player** has a dependency with **Algorithm**.
- **Player** is open for extension because it can be extended to support different algorithms.
- **Player** is closed for modification because it does not need to be modified to support different algorithms.
---
- **Algorithm** is an abstract class that defines the algorithm. It has a **Board** object as a member variable. It also has a method to get the best move.
- **Algorithm** has a dependency with **Board**.
- **Algorithm** is open for extension because it can be extended to support different algorithms.
- **Algorithm** is closed for modification because it does not need to be modified to support different algorithms.











