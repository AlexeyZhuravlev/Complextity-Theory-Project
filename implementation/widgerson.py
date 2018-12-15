from math import sqrt
from help_functions import color_subset, recalculate_degrees, calculate_greedy_rest


class Widgerson:

    def __init__(self, graph):
        n = len(graph)
        degrees = [len(incident_list) for incident_list in graph]
        border = sqrt(n)
        self.colors = [None] * n
        min_color = 0
        while True:
            max_degree = max(degrees)
            if max_degree < border:
                break
            current_vertex = degrees.index(max_degree)
            min_color = color_subset(graph, graph[current_vertex], self.colors, min_color)
            recalculate_degrees(graph, set(graph[current_vertex]), degrees)
        calculate_greedy_rest(graph, self.colors)

    def get_coloring(self):
        return self.colors
