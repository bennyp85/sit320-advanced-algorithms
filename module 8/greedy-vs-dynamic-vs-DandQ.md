### Divide and Conquer
- **Approach**: Breaks the problem into smaller subproblems, solves them independently, and then combines their solutions.
- **Subproblems**: Subproblems are solved independently.
- **Optimization**: Not specifically designed for optimization problems.
- **Memory Usage**: Generally doesn't store solutions to subproblems.
- **Examples**: Merge Sort, Quick Sort.

### Dynamic Programming (DP)
- **Approach**: Breaks the problem into overlapping subproblems, solves them, and stores their solutions - typically using a memory-based table approach.
- **Subproblems**: Solves overlapping subproblems and reuses their solutions.
- **Optimization**: Often used for optimization problems.
- **Memory Usage**: Stores the solutions to subproblems to avoid redundant computations.
- **Examples**: Fibonacci sequence (using memoization), Knapsack problem.

### Greedy Algorithms
- **Approach**: Makes the locally optimal choice at each step in the hope of finding a global optimum.
- **Subproblems**: Doesn't necessarily solve subproblems; focuses on immediate, locally optimal decisions.
- **Optimization**: Often used for optimization problems.
- **Memory Usage**: Generally doesn't need to store multiple solutions to subproblems.
- **Examples**: Kruskal's algorithm for Minimum Spanning Tree, Greedy Activity Selection.
