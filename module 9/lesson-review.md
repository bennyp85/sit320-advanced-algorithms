# School of Information Technology, Deakin University
# SIT320 — Advanced Algorithms
## Module Nine: Linear Programming

### Lesson Review
- Some key terms related to linear programming are:
    - **Objective function:** The function that is to be maximized or minimized.
    - **Constraints:** The conditions that must be satisfied by the solution.
    - **Feasible region:** The region of the graph that satisfies all the constraints.
    - **Optimal solution:** The solution that maximizes or minimizes the objective function.
- Techniques for solving linear programming problems include:
    - **Graphical solution:** A method for solving linear programming problems by plotting the constraints and the objective function on a graph.
    - **Simplex:** A method for solving linear programming problems by traversing the feasible region using pivot operations.
    - **LU decomposition** of a matrix A is a factorization of A into a lower triangular matrix L and an upper triangular matrix U such that A = LU.
    - The LU decomposition can be used to solve linear equations of the form Ax = b by first solving Ly = b using forward substitution and then solving Ux = y using backward substitution.

### Task 1 - Graphical Solution
- This was an interseting task as no feasible region was found.
- The frist two constraint were plotted and the region was a lower bound.
- The third constraint was plotted and the region was an upper bound.
- I was somewhat confused about the feasible region. I Originally thought that I made a mistake.
- Reflectining on this, I think that there is value in a task with no feasible region.
- This made me think more critically about the problem and the constraints.
- There seems to be a lot of insighted gained from understanding why there is no feasible region.

### Task 2 - Code for Solving Linear Equations (y = Ax) using LU Decomposition
- LU decomposition has three steps involved:
    - Decomposition of the matrix A into L and U.
    - Forward substitution to solve Ly = b.
    - Backward substitution to solve Ux = y.
- LU decomposition takes the original matrix and decomposes it into two matrices, L and U.
- The matrix L is a lower triangular matrix with ones on the diagonal.
- The matrix U is an upper triangular matrix.
- **Computational complexity:** O(n^3)
- **Space complexity:** O(n^2)

### Task 3 - Solve Linear Program Using Simplex
- Simplex is a step by step process that converges to the optimal solution.
- This is acheived by traversing the feasible region using pivot operations.
- The pivot operations are:
    - **Pivot row:** The row that is selected for the pivot operation.
        - We find the pivot row by dividing the right-hand side of each constraint by the corresponding element in the pivot column.
    - **Pivot column:** The column that is selected for the pivot operation.
        - The pivot column is the column with the most negative value in the bottom row.
    - **Pivot element:** The element that is selected for the pivot operation.
        - The pivot element is the element in the pivot row and pivot column.
- **Computational complexity:** This is interesting as we performed hand calulations.
    - To compute the complexity we look at each basic operation. We can then count how many basic operations are performed.

### Conclusion

### Reading Reflection