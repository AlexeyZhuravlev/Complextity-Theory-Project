def color_subset(graph, vertices_set, colors, min_color):

    def dfs(v, shift):
        colors[v] = min_color + shift
        for incident in graph[v]:
            if incident in vertices_set:
                if colors[incident] is None:
                    if not dfs(incident, 1 - shift):
                        return False
                elif colors[incident] == colors[v]:
                    return False
        return True
    for vertex in vertices_set:
        if colors[vertex] is None:
            if not dfs(vertex, 0):
                return None
    return min_color + 2


def recalculate_degrees(graph, important_verteces, degrees):
    for vertex in important_verteces:
        degrees[vertex] = 0
        for incident in graph[vertex]:
            degrees[incident] -= 1


def calculate_greedy_rest(graph, colors):
    n = len(graph)
    for vertex in range(n):
        if colors[vertex] is None:
            neighbour_colors = set(range(n))
            for neighbour in graph[vertex]:
                if colors[neighbour] is not None and colors[neighbour] in neighbour_colors:
                    neighbour_colors.remove(colors[neighbour])
            colors[vertex] = min(neighbour_colors)


def get_all_neighbours(graph, important_vertices, colors):
    neighbours = set()
    for vertex in important_vertices:
        for incident in graph[vertex]:
            if colors[incident] is None and incident not in important_vertices:
                neighbours.add(incident)
    return neighbours
