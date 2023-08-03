## Summary

- **Strongly Connected Components (SCCs)**:
  - SCC in a directed graph `G = (V,E)` exists if for every `v, w` in `V`, there's a path from `v` to `w` and vice versa.
  - SCCs are essential for community detection or clustering in applications like Facebook, Twitter, or telco offers.

- **Why SCCs Matter**:
  - Helps in performing targeted analysis and profiling on user communities or clusters.

- **Algorithm for SCCs**:
  - Basic approach uses DFS to determine paths between every pair `(u, v)`. But it's inefficient with a complexity of `O(n^2)`.
  - Choosing a starting node in DFS affects outcome. So, apply DFS repeatedly from different nodes to cover the entire graph, leading to a 'depth-first forest'.
  - To determine SCCs:
    1. Apply DFS and record each node's finishing time.
    2. Reverse all edges.
    3. Apply DFS again, starting nodes based on reverse of their original finishing times.
    4. SCCs are trees in this second DFS forest.

- **Reference**:
  - Coreman et al.'s "Binary Search Trees, Chapter 22".
