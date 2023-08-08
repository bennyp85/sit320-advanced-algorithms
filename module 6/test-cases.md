### Test Cases for Bellman-Ford Algorithm

#### Test Case 1: Simple Connected Graph

```plaintext
Vertices: A, B, C
Edges: (A, B, 1), (B, C, 2), (A, C, 4)
Source: A

Expected Output:
Distance from A to A: 0
Distance from A to B: 1
Distance from A to C: 3
```

#### Test Case 2: Graph with Negative Weights

```plaintext
Vertices: A, B, C
Edges: (A, B, -1), (B, C, 2), (A, C, 4)
Source: A

Expected Output:
Distance from A to A: 0
Distance from A to B: -1
Distance from A to C: 1
```

#### Test Case 3: Graph with Negative Cycle

```plaintext
Vertices: A, B, C
Edges: (A, B, 1), (B, C, 2), (C, A, -4)
Source: A

Expected Output:
"Graph contains a negative-weight cycle"
```

### Test Cases for Floyd-Warshall Algorithm

#### Test Case 1: Simple Connected Graph

```plaintext
Vertices: A, B, C
Edges: (A, B, 1), (B, C, 2), (A, C, 4)

Expected Output:
Distance from A to A: 0
Distance from A to B: 1
Distance from A to C: 3
Distance from B to A: ∞
Distance from B to B: 0
Distance from B to C: 2
Distance from C to A: ∞
Distance from C to B: ∞
Distance from C to C: 0
```

#### Test Case 2: Complete Graph with Negative Edges

```plaintext
Vertices: A, B, C
Edges: (A, B, -1), (B, C, 2), (A, C, 4), (B, A, 1), (C, A, -2), (C, B, 1)

Expected Output:
Distance from A to A: 0
Distance from A to B: -1
Distance from A to C: -3
Distance from B to A: -2
Distance from B to B: 0
Distance from B to C: 1
Distance from C to A: -2
Distance from C to B: -3
Distance from C to C: 0
```
