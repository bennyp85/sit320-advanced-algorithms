1. **Boolean Logic:** This is used in conditionals (if statements), where you're often checking if certain conditions are true or false. 

    ```python
    if condition1 and condition2:
        # Execute some code
    ```

2. **Graph Theory:** The dependency graph of classes or modules in a software system can be considered a directed graph, a concept from graph theory in mathematics. Nodes represent classes or modules, and edges represent dependencies.

    ```plain
    ClassA ----> ClassB ----> ClassC
    (Node)      (Edge)      (Node)
    ```

3. **Set Theory:** Set theory can be relevant when thinking about groups of objects, and can come into play when dealing with collections of objects in your code.

    ```python
    group_of_objects = set([object1, object2, object3])
    ```

4. **Functions:** In programming, functions/methods can be thought of in mathematical terms. They take input(s), process them, and produce output(s).

    ```python
    def add(x, y):
        return x + y
    ```

5. **Recursion:** The concept of recursion in computer science, which is central to the minimax algorithm discussed in the Tic-Tac-Toe code, has a mathematical basis. Recursive functions call themselves to solve smaller subproblems, a structure similar to mathematical induction.

    ```python
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    ```

6. **Game Theory:** The minimax algorithm is derived from game theory, a branch of mathematics that deals with decision-making.

    ```python
    def minimax(node, depth, maximizingPlayer):
        if depth == 0 or node is a terminal node:
            return the heuristic value of node

        if maximizingPlayer:
            value = -infinity
            for each child of node:
                value = max(value, minimax(child, depth - 1, false))
            return value

        else:
            value = +infinity
            for each child of node:
                value = min(value, minimax(child, depth - 1, true))
            return value
    ```

7. **Matrix and Arrays:** In some games like Tic-Tac-Toe, the game board can be represented as a two-dimensional grid or matrix, which is a mathematical concept.

    ```python
    board = [['', '', ''],
             ['', '', ''],
             ['', '', '']]
    ```
