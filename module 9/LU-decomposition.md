# LU Decomposition Reference Sheet

## Overview
LU Decomposition is a method for factorizing a square matrix `A` into the product of a lower triangular matrix `L` and an upper triangular matrix `U`.

---

## Key Concepts

### Lower Triangular Matrix (L)
Matrix with all entries above the diagonal set to zero.

### Upper Triangular Matrix (U)
Matrix with all entries below the diagonal set to zero.

---

## Algorithm Steps

1. **Initialization**: Start with a square matrix `A` of dimensions `n x n`.

2. **Factorization**: Decompose `A` into `L` and `U` such that `A = L * U`

   - For each row, eliminate elements below the diagonal by subtracting multiples of the row from lower rows.

3. **Solve for `L` and `U`**: Use row operations to fill in the entries of `L` and `U`.
   - The three primary row operations are:
       1. **Row Swap**: Swap two rows.
       2. **Row Scale**: Multiply a row by a constant.
       3. **Row Add**: Add a multiple of one row to another row.

4. **Solve Linear Equations**: To solve `Ax = b`:

   1. **Forward Substitution**: Solve `Ly = b` to find `y`.
   2. **Backward Substitution**: Solve `Ux = y` to find `x`.

---
## Applications
- Solving systems of linear equations
- Matrix inversion
- Determinant computation

## Ethical Considerations
- Accurate and efficient algorithms can be crucial in systems where mistakes can be costly or dangerous.