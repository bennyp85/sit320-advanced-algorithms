### Bellman-Ford Algorithm

The Bellman-Ford algorithm is a graph search algorithm that computes the shortest paths from a single source vertex to all of the other vertices in a weighted graph. It's named after its developers, Richard Bellman and Lester Ford.

#### Key Characteristics

1. **Handles Negative Weights:** Unlike Dijkstra's algorithm, Bellman-Ford can handle graphs with negative weight edges.
2. **Detects Negative Cycles:** The algorithm can also detect and report if there's a negative-weight cycle in the graph.
3. **Slower than Dijkstra's Algorithm:** Its time complexity is \(O(|V||E|)\).

#### How It Works

- **Initialization:** Set the distance to the source vertex to 0 and the distance to all other vertices to infinity.
- **Edge Relaxations:** Check if the distance to the destination vertex can be shortened.
- **Repeat Relaxations:** Steps are repeated \(|V| - 1\) times.
- **Negative Cycle Detection:** If you can still relax an edge after \(|V|-1\) iterations, there must be a negative-weight cycle.

#### Pseudocode

```plaintext
function BellmanFord(graph, source):
    distance[source] = 0
    for each vertex v in graph:
        if v is not source:
            distance[v] = infinity
            predecessor[v] = undefined

    repeat |V|−1 times:
        for each edge (u, v) with weight w in graph:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                predecessor[v] = u

    for each edge (u, v) with weight w in graph:
        if distance[u] + w < distance[v]:
            report "Graph contains a negative-weight cycle"
    
    return distance, predecessor
```

#### Applications

- Network routing protocols.
- Finding arbitrage opportunities in currency exchange.
- Shortest path problems in transportation and logistics.
