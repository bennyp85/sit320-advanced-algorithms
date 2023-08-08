### Floyd-Warshall Algorithm

The Floyd-Warshall algorithm is used to find the shortest paths between all pairs of vertices in a weighted graph. It works with both directed and undirected graphs and allows negative edge weights, as long as there are no negative cycles.

#### Key Characteristics

1. **All-Pairs Shortest Path:** Unlike algorithms like Dijkstra's that find the shortest path from a single source, Floyd-Warshall computes the shortest paths between every pair of vertices.
2. **Handles Negative Weights:** It can handle negative weight edges, but the presence of negative cycles can lead to incorrect results.
3. **Time Complexity:** The time complexity of the Floyd-Warshall algorithm is \(O(|V|^3)\), where \(|V|\) is the number of vertices.

#### How It Works

The algorithm uses a dynamic programming approach, building up solutions to subproblems. It considers all pairs of nodes and systematically tries all possible paths between each pair to find the shortest one.

#### Pseudocode

```plaintext
function FloydWarshall(graph):
    for each vertex v in graph:
        distance[v][v] = 0

    for each edge (u, v) with weight w in graph:
        distance[u][v] = w

    for k from 1 to |V|:
        for i from 1 to |V|:
            for j from 1 to |V|:
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance
```

#### Applications

- Finding shortest paths in networking for routing.
- In computer graphics for solving problems like mesh simplification.
- For various optimization problems in logistics and transportation.

The Floyd-Warshall algorithm's main advantage is its simplicity and the fact that it can be used on graphs with negative weight edges. Its cubic time complexity makes it less suitable for very large graphs.
