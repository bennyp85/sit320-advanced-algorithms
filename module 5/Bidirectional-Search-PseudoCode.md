```python
function BidirectionalSearch(s, t, G):
    if s == t:
        return [s]

    # Create two sets to keep track of visited nodes from s and t
    visited_from_s = {s}
    visited_from_t = {t}

    # Create dictionaries to store parent information for path reconstruction
    parent_from_s = {}
    parent_from_t = {}

    # Frontiers for BFS starting from s and t
    frontier_from_s = [s]
    frontier_from_t = [t]

    while frontier_from_s and frontier_from_t:
        # Expand the BFS from s
        next_frontier_s = []
        for node in frontier_from_s:
            for neighbor in node.neighbors:
                if neighbor not in visited_from_s:
                    visited_from_s.add(neighbor)
                    parent_from_s[neighbor] = node
                    next_frontier_s.append(neighbor)

                    if neighbor in visited_from_t:
                        # We found a meeting point! 
                        # Reconstruct the path from s to t through neighbor
                        return reconstruct_path(s, t, neighbor, parent_from_s, parent_from_t)

        # Expand the BFS from t
        next_frontier_t = []
        for node in frontier_from_t:
            for neighbor in node.neighbors:
                if neighbor not in visited_from_t:
                    visited_from_t.add(neighbor)
                    parent_from_t[neighbor] = node
                    next_frontier_t.append(neighbor)

                    if neighbor in visited_from_s:
                        # We found a meeting point! 
                        # Reconstruct the path from t to s through neighbor
                        return reconstruct_path(t, s, neighbor, parent_from_t, parent_from_s)

        frontier_from_s = next_frontier_s
        frontier_from_t = next_frontier_t

    return None  # No path found


function reconstruct_path(source, target, meeting_point, parent_from_source, parent_from_target):
    # Build the path from source to meeting point
    path_from_source = [meeting_point]
    while meeting_point != source:
        meeting_point = parent_from_source[meeting_point]
        path_from_source.append(meeting_point)
    
    # Build the path from target to meeting point
    path_from_target = []
    current = parent_from_target[meeting_point]
    while current != target:
        path_from_target.append(current)
        current = parent_from_target[current]

    # Combine the two paths to get the full path from source to target
    path_from_source.reverse()  # Reverse since we built it backwards
    return path_from_source + path_from_target
```