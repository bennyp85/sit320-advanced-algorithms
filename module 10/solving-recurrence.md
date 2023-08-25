### Substitution Method

The substitution method is used to analyze the time complexity of recursive algorithms by making educated guesses about the solution, and then using mathematical induction to prove or disprove the guess.

**Example:**
Suppose we have the recurrence relation `T(n) = T(n/2) + O(1)`. A guess could be `T(n) = O(log n)`. We can then prove this guess using induction.

**Steps:**
1. **Guess**: `T(n) = c * log n`.
2. **Prove**: Use induction to prove that this guess is correct by substituting into the recurrence relation.

### Master Theorem

The master theorem provides a general solution to divide-and-conquer recurrence relations, enabling quick analysis of the time complexity.

**Example:**
For a recurrence of the form `T(n) = a * T(n/b) + f(n)`, the master theorem gives the following solution:
- If `f(n) = O(n^c)` where `c < log_b(a)`, then `T(n) = Θ(n^(log_b(a)))`.
- If `f(n) = Θ(n^(log_b(a)))`, then `T(n) = Θ(n^(log_b(a)) * log n)`.
- If `f(n) = Ω(n^c)` where `c > log_b(a)`, then `T(n) = Θ(f(n))`.

### Recursion Tree Method

The recursion tree method visualizes the recurrence as a tree where each node represents the cost at each level of recursion. By summing up the costs at all levels, the time complexity can be deduced.

**Example:**
Consider the recurrence `T(n) = 2 * T(n/2) + O(n)`. We can visualize this using a recursion tree:
```
         O(n)
        /    \
     O(n/2)  O(n/2)
    /    \    /   \
O(n/4) ...  O(n/4) ...
``` 

**Steps:**
1. **Construct the Tree**: Break down the recurrence into a tree structure.
2. **Calculate Costs**: Calculate the cost at each level.
3. **Sum the Costs**: Sum the costs at all levels to deduce the time complexity.

In this case, there are `log n` levels with a total cost of `O(n)`, so `T(n) = O(n log n)`.
