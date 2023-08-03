## Key Terms and Definitions:

### Breadth First Search (BFS):
- **BFS:** A strategy to explore a graph level-by-level. It's implemented using a Queue data structure.
- **Visualization:** If at a node, BFS explores nodes based on how many hops are needed to reach them. Nodes that are one hop away are explored before nodes that are two hops away, and so on.
  
### BFS Complexity:
- **Non-Recursive:** Unlike DFS, BFS does not use recursion.
- **BFS Tree:** Nodes are grouped based on the number of hops needed to reach them. Nodes B and E might be reached in one hop, while nodes C, F, and D might require two hops, and so on.
- **Running Time Complexity:** Not explicitly mentioned, but likely related to the number of nodes and edges.

### Applications of BFS:
- **Shortest Path Algorithm:** Determines the minimum number of hops required to go from one node to another.
- **Bipartite Test:** The BFS tree can help in determining if a graph is bipartite or not.

### Miscellaneous Information:
- **Connected Components:** BFS can find all the nodes reachable from the starting point, revealing all connected components.

### Resources:
- **CLRS:** Coreman, T. and Leiserson, C. and Rivest, R. and Stein, C. "Binary Search Trees", Chapter 22, Chapter 12.
- **GTG:** Goodrich, Tamassia, Goldwasser, "Data Structures and Algorithms in Python", Chapter 14.

