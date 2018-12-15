from math import log2, sqrt
from itertools import combinations
from help_functions import get_all_neighbours, color_subset, calculate_greedy_rest


class BergerRompel:

    def __init__(self, graph):
        n = len(graph)
        self.colors = [None] * n
        logn = round(log2(n) + 0.5)
        border = round(sqrt(n / logn) + 0.5)
        min_color = 0
        while True:
            current_size = 0
            current_s = set()
            current_neighbours = set()
            for vertex in range(n):
                count = 0
                local_set = set()
                for incident in graph[vertex]:
                    if self.colors[incident] is None and incident not in current_neighbours\
                            and incident not in current_s:
                        local_set.add(incident)
                        count += 1
                if count >= border:
                    current_neighbours.update(local_set)
                    current_s.add(vertex)
                    current_size += 1
                if current_size >= 3 * logn:
                    for combination in combinations(current_s, logn):
                        neighbours = get_all_neighbours(graph, combination, self.colors)
                        result = color_subset(graph, neighbours, self.colors, min_color)
                        if result is None:
                            for neighbour in neighbours:
                                self.colors[neighbour] = None
                        else:
                            min_color = result
                            break
                    break
            if current_size < 3 * logn:
                for vertex in current_s:
                    neighbours = get_all_neighbours(graph, [vertex], self.colors)
                    if len(neighbours) > 0:
                        min_color = color_subset(graph, neighbours, self.colors, min_color)
                break
        calculate_greedy_rest(graph, self.colors)

    def get_coloring(self):
        return self.colors
