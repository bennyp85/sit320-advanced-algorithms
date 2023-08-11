### Longest Common Sub-sequence (LCS)

The Longest Common Sub-sequence (LCS) problem is a classic problem in computer science and bioinformatics. It involves finding the longest sequence of characters that appear in the same order within two sequences, without necessarily being contiguous.

#### 1. Problem Statement:
Given two sequences `X` and `Y`, find the longest sequence of characters that are common to both `X` and `Y`.

#### 2. Applications:
- Text comparison (such as in version control systems).
- DNA sequence alignment in bioinformatics.
- Spell checking and correction.

#### 3. Dynamic Programming Solution:
- **Step 1:** Create a table `C` where `C[i][j]` stores the length of the LCS of `X[0..i-1]` and `Y[0..j-1]`.
- **Step 2:** Initialize the first row and first column to 0.
- **Step 3:** Iterate through `X` and `Y`, and fill in the table according to the following rules:
  - If `X[i]` is equal to `Y[j]`, then `C[i][j] = C[i-1][j-1] + 1`.
  - Otherwise, `C[i][j] = max(C[i-1][j], C[i][j-1])`.
- **Step 4:** The value `C[m][n]`, where `m` and `n` are the lengths of `X` and `Y`, will be the length of the LCS.
- **Step 5:** You can reconstruct the actual LCS by backtracking through the table `C`.

#### 4. Complexity:
- Time Complexity: `O(m * n)`, where `m` and `n` are the lengths of the sequences.
- Space Complexity: `O(m * n)` for storing the table `C`.

#### 5. Example:
Consider two sequences `X = "ABCBDAB"` and `Y = "BDCAB"`. The LCS is `"BCAB"`.

#### Conclusion:
The LCS problem is a foundational problem in computer science, with various real-world applications. By employing dynamic programming, the problem can be solved efficiently. It's an illustrative example of how complex problems can be broken down into subproblems, a key concept in algorithm design.
