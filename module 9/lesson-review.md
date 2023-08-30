# School of Information Technology, Deakin University
# SIT320 — Advanced Algorithms
## Module Nine: Linear Programming

### [ChatGPT Link](https://chat.openai.com/share/cc87a452-8f00-422a-b5e9-2e3c93f623d8)
### [GitHub Link](https://github.com/bennyp85/sit320-advanced-algorithms/tree/master/module%209)
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
- I was somewhat confused about the feasible region. I originally thought that I made a mistake.
- Reflectining on this, I think that there is value in a task with no feasible region.
- This made me think more critically about the problem and the constraints.
- The insight I gained from this task was that the constraints were not compatible.

### Task 2 - Code for Solving Linear Equations (y = Ax) using LU Decomposition
- LU decomposition has three steps involved:
    - Decomposition of the matrix A into L and U.
    - Forward substitution to solve Ly = b.
    - Backward substitution to solve Ux = y.
- LU decomposition takes the original matrix and decomposes it into two matrices, L and U.
- The matrix L is a lower triangular matrix with zeros in the upper triangle.   
- The matrix U is an upper triangular matrix with zeros in the lower triangle.
- **Computational complexity:** O(n^3) Note: There are more efficient ways to solve this problem. Such as solutions based on the Coppersmith–Winograd algorithm.
- **Space complexity:** O(n^2)

### Task 3 - Solve Linear Program Using Simplex
- Simplex is a step by step process that converges to the optimal solution.
- This is acheived by traversing the feasible region using pivot operations.
- Simnplex traverses the outer edges of the feasible region.
- There are other algorithms that traverse the interior of the feasible region.
- The pivot operations are:
    - **Pivot row:** The row that is selected for the pivot operation.
        - We find the pivot row by dividing the right-hand side of each constraint by the corresponding element in the pivot column.
    - **Pivot column:** The column that is selected for the pivot operation.
        - The pivot column is the column with the most negative value in the bottom row.
    - **Pivot element:** The element that is selected for the pivot operation.
        - The pivot element is the element in the pivot row and pivot column.
- **Computational complexity:** This is interesting as we performed hand calulations.
    - To compute the complexity we could look at each basic operation. We can then count how many basic operations are performed.

### Some interesting takeaways from this module
- I forgot how much I enjoyed doing hand calculations. It's different to coding, but the same level of care is required.
- Formulating purely math based ideas into code came with it's own challenges.
- I would be interested to learn about design patterns that are specific to math based problems.
- I believe numpy has a lot of these patterns built in.
- Don't be shy if I think there is a mistake in the task. I learnt more by asking questions. 
- Using optimisation algorithms can have a profound impact on society. That being said, it's important to understand the implications of these algorithms.
- An example of this is resource allocation. If we use an optimisation algorithm to allocate resources, we need to be aware of how this directly impacts people.

### Conclusion
- Constraints and feasible regions are two key topics in linear programming. They allow us to find optimal solutions to problems. We looked at three ways to solve linear programming probelms. Graphically, which is the most basic and only really involved plotting a graph. Through LU decompostion, which involved creating two matricies L and U, and then computing the elements of each. Forward and backward substitution were used to solve the linear equations. The final method was simplex which we completed by hand calculations. The Simplex method traverses the feasible region using pivot operations.
- I thoroughly enjoyed this module. I found it to be a good mix of theory and practical. I also enjoyed the philosophical aspects of this module. I think it's important to understand the implications of optimisation algorithms. 
### Readings
- **Introduction to Algorithms**: Cormen, Leiserson, Rivest, Stein
    - Part VII: Selected Topics
        - Chapter 29: Linear Programming
- **LibreTexts**: https://tinyurl.com/4sa6na5n
    - 4.2: Maximization By The Simplex Method
- **AtoZMAth.com**: https://tinyurl.com/22jknfe3
    - Simplex Method Calculator
- **Matrix Reshish**: https://matrix.reshish.com/gauss-jordanElimination.php
    - Gauss-Jordan Elimination Calculator
- **Desmos**: https://www.desmos.com/calculator
    - Online Graphing Calculator