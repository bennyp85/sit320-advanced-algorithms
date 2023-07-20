```
+------------------------------------+
|          <<abstract>>              |
|           Algorithm                |
+------------------------------------+
| - boardGame: Board                 |
+---------------------------------------------------+
| + __init__(boardGame: Board)                      |
| + bestMove(boardGame: Board, letter: string): int |
+---------------------------------------------------+

+-------------------------------+
|         <<abstract>>          |
|            Board              |
+-------------------------------+
| - dimension: int              |
+----------------------------------------------------+
| + __init__(dimension: int)                         |
| + createBoard(): void                              |
| + printBoard(): void                               |
| + setCellState(position: int, state: string): void |
| + getCellState(position: int): String              |
| + getBoardState(): dict                            |
| + getBoardDimensions(): int                        |
+----------------------------------------------------+

+----------------------------------+
|          <<abstract>>            |
|           GameLogic              |
+----------------------------------+
| - boardGame: Board               |
+-----------------------------------------------------+
| + __init__(boardGame: Board)                        |
| + chkForWin(): bool                                 |
| + chkForDraw(): bool                                |
| + chkMarkForWin(letter: string): bool               |
| + insertLetter(letter: string, position: int): void |
| + spaceIsFree(position: int): bool                  |
+-----------------------------------------------------+

+-------------------------------+
|        <<abstract>>           |
|           Player              |
+-------------------------------+
| - letter: String              |
| - algorithm: Algorithm        |
+--------------------------------------------------+
| + __init__(letter: String, algorithm: Algorithm) |
| + chooseAlgorithm(algorithm: Algorithm): void    |
| + makeMove(boardGame: Board): Tuple              |
+--------------------------------------------------+
```

- **GameLogic** is an abstract class that defines the game logic. It has a **Board** object as a member variable. It also has methods to check for a win, check for a draw, check for a win for a specific letter, insert a letter in a specific position, and check if a space is free.
- **GameLogic** has associations with **Board** and **Algorithm**.
- **GameLogic** subclasses inherit from **GameLogic**.
- **GameLogic** is open for extension because it can be extended to support different games.
- **GameLogic** is closed for modification because it does not need to be modified to support different games.
---
- **Board** is an abstract class that defines the board. It has a **Board** object as a member variable. It also has methods to create the board, print the board, set the state of a cell, get the state of a cell, get the state of the board, and get the dimensions of the board.
- **Board** has associations with **GameLogic** and **Player** and **Algorithm**.
- **Board** subclasses inherit from **Board**.
- **Board** is open for extension because it can be extended to support different boards.
- **Board** is closed for modification because it does not need to be modified to support different boards.
---
- **Player** is an abstract class that defines the player. It has a letter and an algorithm as member variables. It also has methods to choose an algorithm and make a move.
- **Player** has associations with **Algorithm** and **Board**.
- **Player** subclasses inherit from **Player**.
- **Player** is open for extension because it can be extended to support different algorithms.
- **Player** is closed for modification because it does not need to be modified to support different algorithms.
---
- **Algorithm** is an abstract class that defines the algorithm. It has a **Board** object as a member variable. It also has a method to get the best move.
- **Algorithm** has associations with **Board** and **Player** and **GameLogic**.
- **Algorithm** subclasses inherit from **Algorithm**.
- **Algorithm** is open for extension because it can be extended to support different algorithms.
- **Algorithm** is closed for modification because it does not need to be modified to support different algorithms.











