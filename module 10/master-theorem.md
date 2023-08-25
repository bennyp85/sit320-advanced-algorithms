### Master Theorem

The Master Theorem is a powerful tool used to determine the time complexity of divide-and-conquer algorithms. It provides solutions for recurrence relations of the form `T(n) = a * T(n/b) + f(n)`, where:

- `a`: Number of subproblems at each level of recursion.
- `b`: Factor by which the problem size is reduced at each level.
- `f(n)`: Time taken to solve the problem at the current level (not including recursive calls).

#### Three Cases of Master Theorem

##### Case 1
If `f(n) = O(n^c)` where `c < log_b(a)`, then the time complexity is:
T(n) = Θ(n^(log_b(a)))
**Explanation**: In this case, the time complexity is dominated by the leaves of the recursion tree. The work done at the higher levels of the tree is relatively small.

##### Case 2
If `f(n) = Θ(n^(log_b(a)))`, then the time complexity is:
T(n) = Θ(n^(log_b(a)) * log n)
**Explanation**: Here, the work done at each level of the tree is roughly the same. The total time complexity is a combination of the work at each level and the number of levels, which is logarithmic.

##### Case 3
If `f(n) = Ω(n^c)` where `c > log_b(a)`, and if `a * f(n/b) ≤ k * f(n)` for some constant `k < 1` and sufficiently large `n`, then the time complexity is:
T(n) = Θ(f(n))
**Explanation**: In this case, the majority of the work is done at the root of the recursion tree. The work done at the lower levels is relatively small, so the time complexity is determined by the work at the current level.

#### Example
Consider the recurrence relation `T(n) = 2 * T(n/2) + O(n)`. Applying the Master Theorem, we fall into Case 2 with `a = 2`, `b = 2`, and `f(n) = O(n)`. The solution is:
T(n) = Θ(n * log n)

#### Conclusion
The Master Theorem simplifies the analysis of divide-and-conquer algorithms by categorizing recurrences into three main cases. It provides quick solutions to many recurrence relations, but it has limitations and may not apply to all recurrence forms.
Kv