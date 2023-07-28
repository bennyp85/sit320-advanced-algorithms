## Digraphs (Directed Graphs)

A digraph, or directed graph, is a set of vertices and a collection of directed edges (often called "arcs" or "arrows"). Each edge has an initial vertex (or "tail") and a terminal vertex (or "head").

### Key Characteristics:

1. **Directed Edges**: Edges in digraphs have a direction. An edge from vertex `A` to vertex `B` doesn't imply a connection from `B` to `A`.

2. **Adjacency**: Vertex `A` is said to be adjacent to vertex `B` if there's an edge that starts from `A` and ends in `B`.

3. **In-degree and Out-degree**: 
    - The `in-degree` of a vertex is the number of edges coming into it.
    - The `out-degree` of a vertex is the number of edges going out of it.

4. **Weighted Digraph**: If each edge in the digraph has an associated weight (or cost), then it's termed a weighted digraph.

5. **Paths and Cycles**:
    - A path in a digraph is a sequence of vertices where each adjacent pair is connected by an edge.
    - A cycle in a digraph is a path that starts and ends at the same vertex.

### Types of Digraphs:

1. **Simple Digraph**: A digraph with no loops (edges from a vertex to itself) and no multiple arcs (more than one edge in the same direction between the same pair of vertices).

2. **Acyclic Digraph (DAG)**: A directed graph with no cycles. DAGs are fundamental in computer science and have applications in tasks like scheduling.

3. **Strongly Connected Digraph**: For every pair of vertices `A` and `B`, if there's a path from `A` to `B` and a path from `B` to `A`, then the digraph is strongly connected.

### Applications of Digraphs:

1. **Web Crawling**: The web can be represented as a digraph, where each webpage is a vertex and hyperlinks between pages are directed edges.

2. **Dependency Resolution**: In systems like package managers, tasks with dependencies can be modeled as digraphs to resolve the order of operations.

3. **State Machines**: Representing possible states and transitions between them.

4. **Citation Networks**: Scientific papers citing other papers form a natural digraph.

### Algorithms:

Several graph algorithms can be applied specifically to digraphs or need special consideration when used with digraphs. Examples include:
- Topological Sorting (specific to DAGs)
- Strongly Connected Components
- Dijkstra's and Bellman-Ford for shortest paths

### Conclusion:

Digraphs offer a robust way to model many real-world systems, especially those where relationships have a direction. From software dependencies to recommendation engines, digraphs play a foundational role in computer science and many other domains.
