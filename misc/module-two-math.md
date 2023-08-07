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

8. **Probability and Statistics:** Used in a variety of domains, including AI and machine learning, to predict outcomes based on data.

    ```python
    import random
    outcome = random.choice(['win', 'lose', 'draw'])
    ```

9. **Combinatorics:** The study of combinations, arrangements, and subsets of collections. Useful in algorithms that need to consider all potential combinations of a set of items.

    ```python
    from itertools import combinations
    all_combinations = list(combinations(['a', 'b', 'c'], 2))
    ```

10. **Linear Algebra:** This is the branch of mathematics concerning vectors and matrices. It's fundamental in computer graphics, physics simulations, and machine learning.

    ```python
    import numpy as np
    matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
    inverted_matrix = np.linalg.inv(matrix)
    ```

11. **Calculus:** Especially in machine learning and physics simulations, differential and integral calculus play a crucial role. For instance, gradient descent is a calculus-based optimization algorithm.

    ```python
    def gradient_descent_update(current_value, gradient, learning_rate):
        return current_value - learning_rate * gradient
    ```

12. **Number Theory:** Concerns properties and relationships of numbers, especially integers. Cryptography, for example, is heavily reliant on number theory concepts like prime numbers.

    ```python
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    ```

13. **Geometry:** Used extensively in computer graphics, computer vision, and robotics. Concepts like points, lines, polygons, and transformations are foundational.

    ```python
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    ```
