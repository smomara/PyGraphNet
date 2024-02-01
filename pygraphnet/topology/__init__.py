import heapq

__all__ = ['shortest_distance']

# Distance and paths
def shortest_distance(g, source=None, target=None, weights=None):
    if source is None:
        return {v: shortest_distance(g, source=v, target=target, weights=weights) for v in g.vertices}
    
    distances = {v: float('inf') for v in g.vertices}
    distances[source] = 0
    visited = set()

    if weights:
        # Djikstra's algorithm for weighted graphs
        queue = [(0, source)]
        while queue:
            dist, current_vertex = heapq.heappop(queue)
            if current_vertex in visited:
                continue
            visited.add(current_vertex)

            for neighbor in g.adj_list[current_vertex]:
                if g.directed:
                    edge = (current_vertex, neighbor)
                else:
                    edge = (current_vertex, neighbor) if (current_vertex, neighbor) in weights else (neighbor, current_vertex)
                weight = weights[edge] if edge in weights else 1
                new_dist = dist + weight

                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(queue, (new_dist, neighbor))
    else:
        # BFS for unweighted graphs
        queue = [source]
        visited.add(source)
        while queue:
            current_vertex = queue.pop(0)
            for neighbor in g.adj_list[current_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    distances[neighbor] = distances[current_vertex] + 1
    
    if target is not None:
        if hasattr(target, '__iter__'):
            return [distances[t] for t in target]
        else:
            return distances[target]

    return distances