### Proving `T(n) = c * log n` using Induction for the Recurrence `T(n) = T(n/2) + O(1)`

#### Base Case
Identify a base case where the recurrence relation is known to hold true. For example, if `T(1) = a`, use this as the base case.

#### Inductive Step
Assume the recurrence relation holds true for a generic case `T(k) = c * log k` for all `k < n`, and show that if it holds for `k`, it must also hold for `n`.

1. **Hypothesis**: Assume the recurrence holds true for all `k < n`, i.e., `T(k) = c * log k`.
   
2. **Inductive Step**: 
   - Start with the recurrence: `T(n) = T(n/2) + O(1)`
   - Substitute our assumption into the recurrence: `T(n) = c * log(n/2) + O(1)`
   - Simplify using the logarithm property: `T(n) = c * log n - c * log 2 + O(1) = c * log n + b` (where `b` is a constant)
   
3. **Conclusion**: Since the assumption holds for our base case, and we've shown it holds for `n`, we can conclude that our guess `T(n) = c * log n` is correct.

#### Remarks
The constant factor `c` may vary depending on the specifics of the recurrence, and the proof would require handling those specifics. The substitution method can require some ingenuity and mathematical skill, as each recurrence might have unique characteristics that need to be addressed.
