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

- **GameLogic** has an association with **Board**, as it uses the board for its game logic functions.
- **Player** has an association with **Algorithm** since it uses an algorithm to determine the best move.
- **Algorithm** class is abstract, indicating other algorithms can be derived from it.
- **Board** stands alone but interacts with both **GameLogic** and **Algorithm** as indicated by their methods.
- **GameLogic** would have an arrow pointing to **Board** to indicate its dependency.
- **Player** would have an arrow pointing to **Algorithm** to indicate its dependency.
- **Algorithm** would have an arrow pointing to **Board** to indicate its dependency.
- **Board** would have arrows pointing to **GameLogic** and **Algorithm** to indicate its dependency.









