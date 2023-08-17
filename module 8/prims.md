## Prim's Algorithm

Prim's algorithm is a method to find the Minimum Spanning Tree (MST) of a connected, undirected graph with weighted edges. A Minimum Spanning Tree is a subset of the edges of the graph that forms a tree and includes every vertex, with the minimum possible total edge weight.

### Algorithm Steps

1. **Initialize**: Select an arbitrary vertex as the starting point and add it to the MST. Initialize a priority queue (or min-heap) with the edges connected to the starting vertex.
2. **Iterate**: Repeat the following steps until all vertices are included in the MST:
   - a. **Extract Minimum Edge**: Extract the edge with the minimum weight from the priority queue.
   - b. **Check Vertex**: If the connected vertex is not already in the MST, add the edge to the MST and the connected vertex to the included vertices.
   - c. **Update Priority Queue**: Add the edges connected to the newly added vertex to the priority queue, excluding any edges that connect to already included vertices.
3. **Result**: The edges added to the MST form the Minimum Spanning Tree of the graph.

### Time Complexity

The time complexity of Prim's algorithm depends on the data structures used:
- Using a binary heap for the priority queue, the time complexity is `O((V + E) * log V)`, where `V` is the number of vertices, and `E` is the number of edges.
- Using a Fibonacci heap, the time complexity can be reduced to `O(E + V * log V)`.

### Applications

Prim's algorithm has various applications, including:
- Network design (e.g., laying out electrical wiring or water supply with minimal cost)
- Clustering algorithms in data mining
- Approximation algorithms for NP-hard problems

### Example

Consider the following undirected graph with weighted edges:

```
A --1-- B
|      / |
2    3   4
|  /     |
C --5-- D
```

Using Prim's algorithm starting from vertex A, the MST would include the edges (A, B), (A, C), and (B, D), with a total weight of 8.

### Summary

Prim's algorithm is a fundamental algorithm in graph theory for finding the Minimum Spanning Tree of a connected, undirected graph. It builds the MST incrementally, selecting the minimum-weight edge at each step, and efficiently finds the MST using a greedy approach.

## Proof of Prim's Algorithm

Prim's algorithm is used to find the Minimum Spanning Tree (MST) of a connected, undirected graph with weighted edges. We'll prove its correctness by showing that it maintains a loop invariant and that the algorithm's greedy choice is safe.

### Definitions

- **Connected Graph**: A graph where there is a path between any pair of vertices.
- **Cut**: A partition of the vertices into two disjoint sets.
- **Crossing Edge**: An edge that connects a vertex from one set in the cut to a vertex in the other set.
- **Safe Edge**: An edge that, when added to the growing tree, maintains the invariant of the tree being part of some MST.

### Loop Invariant

1. **Invariant**: At the start of each iteration, the vertices in the MST constructed so far form a connected component, and the edges chosen are part of some MST of the graph.
2. **Initialization**: Initially, the MST consists of a single, arbitrarily chosen vertex, which trivially satisfies the invariant.
3. **Maintenance**: During each iteration, the algorithm adds the minimum-weight crossing edge that connects a vertex in the MST so far to a vertex outside of it. We'll prove that this choice is safe, thus maintaining the invariant.
4. **Termination**: At termination, all vertices are included in the MST, and the invariant ensures that the edges form an MST.

### Greedy Choice is Safe

We'll prove that the greedy choice made by Prim's algorithm is safe by showing that the minimum-weight crossing edge is always part of some MST.

1. **Cut Property**: Consider a cut that separates the vertices included so far from the rest of the graph. Let `(u, v)` be the minimum-weight crossing edge for that cut.
2. **Assumption**: Assume, for the sake of contradiction, that `(u, v)` is not part of any MST.
3. **Contradiction**: Since the graph is connected, there must be some other edge `(x, y)` in the MST that also crosses the cut. Adding `(u, v)` and removing `(x, y)` would result in a valid spanning tree with lower weight, contradicting the assumption that `(u, v)` is not part of any MST.
4. **Conclusion**: Therefore, the edge `(u, v)` must be part of some MST, and the greedy choice is safe.

### Summary

By showing that Prim's algorithm maintains the loop invariant and that its greedy choice of the minimum-weight crossing edge is always safe, we have proved that Prim's algorithm correctly finds the Minimum Spanning Tree of a connected, undirected graph with weighted edges.

---
### Psedo Code - I think this needs work.
- We can use properties of the Node class to update the status of the node.
```
function Prim(graph):
  for each vertex v in graph:
    key[v] = +∞
    parent[v] = NIL
  key[start_vertex] = 0
  Q = priority_queue(vertices, key)
  
  while Q is not empty:
    u = extract_min(Q)
    for each neighbor v of u:
      if v in Q and weight[u, v] < key[v]:
        parent[v] = u
        key[v] = weight[u, v]
        update_priority(Q, v)
        
  return parent // The parent array represents the MST edges
```