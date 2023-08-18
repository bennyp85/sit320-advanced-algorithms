# School of Information Technology, Deakin University
# SIT320 — Advanced Algorithms
## Module Six — Dynamic Programming

**Summary of Learning:**
- Dynamic programming is a way to solve problems by **breaking them down into smaller subproblems**. The main idea is to identify the subproblems, solve them, and store the solutions. The solutions to the subproblems are then used to solve the original problem. It is well suited to solving optimisation probelms.
- Dynaic programming takes advantage of two properties:
    - **Overlapping subproblems**
        - A property where the same subproblems are solved multiple times. In DP, solutions to these are stored to avoid redundant computations. 
    - **Optimal substructure**
        - A property where the optimal solution of a problem can be constructed from the optimal solutions of its subproblems.
- This can be acheived witha top-down or bottom-up approach
    - **Top-down(Memoization)**is the approach that begins with the complex problem, breaking it into subproblems, and storing solutions.
        - Storing these solution is called memoization and is acheived by storing the results of function calls so that they can be **used again later**
    - **Bottom-up(Tabulation)** is the approach that starts from the simplest subproblem and builds up the solution.
- **Advantages:**
  - Efficiency: Solves problems faster by avoiding redundant calculations.
  - Versatility: Can be applied to a wide range of problems.
- **Disadvantages:**
  - Memory Usage: Storing solutions to subproblems can be memory-intensive.
  - Complexity: Implementation can be complex and requires a deep understanding of the problem.
- In this module we solved three problems; Running Up Stairs, the Longest Common Subsequence (LCS) and the 0/1 Knapsack Problem.

### Running Up Stairs
- The Running Up Stairs problem is a problem where you have a staircase with n steps and can hop 1, 2, or 3 steps at a time. The goal is to find how many possible ways you can run up the stairs.
- This was a good example of a toy problem that can be solved with DP.
- I quickly reailsed that even a modest number of steps would result in a large number of possible combinations. 10 stairs had over 700 combinations.
- Starting with a recursive solution laid the groundwork for the DP solution. The recursive solution was slow and inefficient, but it was easy to see how it could be improved.

### Longest Common Subsequence
- A classical problem in computer science and bioinformatics. A few common examples are spell checkers, plagiarism checkers, and DNA sequence analysis.
- Steps taken to solve the problem:
    - Understand the problem: What are the subproblems? What is the optimal solution?
        - **Subproblems:** 
            - Given prefixes of the two strings, find the longest common subsequence.
            - Given prefixes of the two strings, find the length of the longest common subsequence if the last charascter is the same.
            - Given prefixes of the two strings, find the length of the longest common subsequence if the last charascter is different.
        - **Optimal Solution:**
            - The longest common subsequence of two strings is the longest sequence of characters that appear in the same order in both strings.
    - Choose DP approach: Top-down or bottom-up?
        - **Top-down:** this problem leant itself to a top-down approach. The problem was broken down into subproblems and the solutions were stored.
    - Construct solution:
        - **Backtracking** was used to construct the solution. The matrix was traversed from the bottom right to the top left. If the characters were the same, the character was added to the solution and the matrix was traversed diagonally. If the characters were different, the matrix was traversed either left or up, depending on which value was larger.
- **Complexity:**
    - Time: O(mn)
    - Space: O(mn)
- **Testing**
    - The algorithm was tested with various test cases. The results were as expected.



    
    