## Key Terms and Definitions:

### Learning Goals:
- **DFS and BFS algorithms:** Depth-First Search and Breadth-First Search algorithms used for graph traversal and searching.
- **Bi-partite Graph:** A graph where nodes can be divided into two distinct sets such that no two nodes within the same set are adjacent.
- **Strongly Connected Components:** Subgraphs in a directed graph where each vertex is reachable from every other vertex in the same component.

### Graphs:
- **Graph:** A collection of interconnected entities.
- **Nodes (or Vertices):** The individual points in a graph.
- **Edges:** The connections between nodes in a graph. Can be directed or undirected.
  
### Directed vs. Undirected Graphs:
- **Undirected Graph:** A graph where an edge between two nodes does not have a direction. Represented as G = (V, E), where V is the set of vertices and E is the set of edges.
- **Directed Graph:** A graph where edges have directions, meaning they go from one vertex to another. 
- **Degree:** For an undirected graph, it's the number of edges connected to a node. For a directed graph, it can be in-degree (number of incoming edges) or out-degree (number of outgoing edges).
  
### Graph Representation:
- **Adjacency Matrix:** A matrix representation of a graph where the value at the intersection of row \(i\) and column \(j\) indicates the presence of an edge between nodes \(i\) and \(j\). Symmetry in this matrix can indicate an undirected graph.
- **Linked List:** Another way to represent a graph, especially useful for sparse graphs. Similar to the representation used for Binary Search Trees.
  
### Miscellaneous:
- **Edge membership operation:** Determines if an edge e = {v, w} exists in set E.
- **Neighbour's Query:** Query to retrieve the neighbors of a given node v.

