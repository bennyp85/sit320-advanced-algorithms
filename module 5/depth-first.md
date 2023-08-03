## Key Terms and Definitions:

### Graph Exploration:
- **Depth-First Search (DFS):** A method to explore a graph by diving as deep as possible before backtracking.
- **Graph Exploration Decision:** Choice of the subsequent node (or neighbor) to visit.

### DFS Mechanics:
- **Unvisited:** A state where a vertex has not been explored.
- **In Progress:** A state indicating that a vertex exploration is ongoing.
- **All Done:** A state indicating that a vertex has been completely explored.
- **Timestamps:** Time of marking a vertex as 'In Progress' and time of marking it as 'All Done'.
  
### DFS Complexity:
- **DFS Complexity:** For a single connected component, the complexity is the number of edges, given by O(m), when using linked list representation. For multiple components, it might involve looking at all nodes and edges, potentially being O(m + n).

### Applications of DFS:
- **Topological Sorting:** An ordering of nodes in a graph that respects the dependencies between them. It can solve problems like determining the order to install software packages based on dependencies.
- **Graph Traversal:** Using DFS to explore the graph in different orders - in-order, post-order, and pre-order.

### Miscellaneous Information:
- **Connected Graph:** A graph where there's a path between every pair of vertices.
- **Trees:** Special forms of graphs where there's exactly one path between any two nodes. DFS can be applied to trees just as it is applied to graphs.
  
### Resources:
- **CLRS:** Coreman, T. and Leiserson, C. and Rivest, R. and Stein, C. "Binary Search Trees", Chapter 22, Chapter 12.
- **GTG:** Goodrich, Tamassia, Goldwasser, "Data Structures and Algorithms in Python", Chapter 14.

