# Simplex Method Reference Sheet

## Overview
The Simplex Method is an optimization algorithm for solving linear programming problems.

---

## Key Concepts

### Feasible Region
The set of all points that satisfy the constraints of the linear programming problem.

### Basic Feasible Solution (BFS)
A corner point of the feasible region, usually a starting point for the algorithm.

### Pivot Operation
The act of moving from one BFS to a neighboring BFS in the direction that improves the objective function.

---

## Algorithm Steps

1. **Initialization**: Convert the problem into standard form, and identify an initial Basic Feasible Solution (BFS).
   - Slack variables may be introduced.
   - Objective function should be expressed in standard form.

2. **Optimality Check**: Evaluate the coefficients in the objective function to determine if the current BFS is optimal.
   - If all coefficients are non-positive, the current BFS is optimal.
  
3. **Pivot Step**: Select the entering and leaving variables.
   - **Entering Variable**: Variable with the most negative coefficient in the objective function.
   - **Leaving Variable**: Variable determined by the minimum ratio test.

4. **Row Operations**: Perform row operations to update the tableau and move to the next BFS.

5. **Iterate**: Go back to step 2 and repeat until an optimal solution is found.

---

## Notes

- **Unbounded Feasible Region**: The problem has no finite optimal solution.
- **Infeasible**: No solution exists that satisfies all constraints.

## Ethical Considerations
- Ensure that the objective function and constraints represent ethical and societal values.


