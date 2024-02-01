import heapq

__all__ = ['shortest_distance', 'shortest_path']

"""
distance and paths
    shortest_distance
    shortest_path
    random_shortest_path
    count_shortest_paths
    all_shortest_paths
    all_predecessors
    all_paths
    all_circuits
    pseudo_diameter

graph comparison
    similarity
    vertex_similarity
    isomorphism
    subgraph_isomorphism
    mark_subgraph
    max_cliques

matching and independent sets
    max_cardinality_matching
    max_independent_vertex_set

spanning tree
    min_spanning_tree
    random_spanning_tree

sorting and closure
    dominator_tree
    topological_sort
    transitive_closure

components and connectivity
    label_components
    label_biconnected_components
    label_largest_component
    extract_largest_component
    label_out_component
    vertex_percolation
    edge_percolation
    kcore_decomposition

graph classification
    is_bipartite
    is_DAG
    is_planar
    make_maximal_planar

directionality
    edge_reciprocity
"""

# Distance and paths
def shortest_distance(g, source=None, target=None, weights=None, pred_map=False):
    if source is None:
        return {v: shortest_distance(g, source=v, target=target, weights=weights) for v in g.vertices}
    
    distances = {v: float('inf') for v in g.vertices}
    predecessors = {v: None for v in g.vertices}
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
                    predecessors[neighbor] = current_vertex
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
                    predecessors[neighbor] = current_vertex
    
    if target is not None:
        if hasattr(target, '__iter__'):
            result = [distances[t] for t in target]
        else:
            result = distances[target]
    else:
        result = distances

    return (result, predecessors) if pred_map else result

def shortest_path(g, source, target, weights=None):
    _, pred_map = shortest_distance(g, source, target, weights, pred_map=True)

    if target not in pred_map or pred_map[target] == None:
        return [], []

    path_vertices = [target]
    path_edges = []

    current_vertex = target
    while current_vertex != source:
        predecessor = pred_map[current_vertex]
        path_edges.insert(0, (predecessor, current_vertex))
        path_vertices.insert(0, predecessor)
        current_vertex = predecessor

    return path_vertices, path_edges