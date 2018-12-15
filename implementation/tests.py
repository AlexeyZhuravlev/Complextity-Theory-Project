import unittest
import random
from unittest import TestCase
from widgerson import Widgerson
from berger_rompel import BergerRompel
import sys

sys.setrecursionlimit(2000)


def check_coloring_correct(graph, coloring):
    n = len(graph)
    flag = True
    for vertex in range(n):
        for incident in graph[vertex]:
            if coloring[vertex] == coloring[incident]:
                flag = False
    return flag


def bernoulli(p):
    return random.uniform(0, 1) <= p


def generate_random_graph(n, m, l, p):
    total = n + m + l
    graph = []
    for i in range(total):
        graph.append([])
    for i in range(n):
        for j in range(m):
            if bernoulli(p):
                graph[i].append(n + j)
                graph[n + j].append(i)
        for k in range(l):
            if bernoulli(p):
                graph[i].append(n + m + k)
                graph[n + m + k].append(i)
    for j in range(m):
        for k in range(l):
            if bernoulli(p):
                graph[n + j].append(n + m + k)
                graph[n + m + k].append(n + j)
    return graph


class IntegrationWidgersonTest(TestCase):

    def test_widgerson_manual(self):
        graph = [[1, 2], [0, 2], [0, 1]]
        coloring = Widgerson(graph).get_coloring()
        self.assertTrue(check_coloring_correct(graph, coloring))
        graph = [[], [], []]
        coloring = Widgerson(graph).get_coloring()
        self.assertTrue(check_coloring_correct(graph, coloring))
        graph = [[1], [0], [3], [2]]
        coloring = Widgerson(graph).get_coloring()
        self.assertTrue(check_coloring_correct(graph, coloring))

    def test_widgerson_stress(self):
        graph = generate_random_graph(300, 300, 400, 0.5)
        coloring = Widgerson(graph).get_coloring()
        self.assertTrue(check_coloring_correct(graph, coloring))
        print("Widgerson: n = 1000, p = 0.5:", max(coloring) + 1, "colors")
        graph = generate_random_graph(300, 300, 400, 0.2)
        coloring = Widgerson(graph).get_coloring()
        self.assertTrue(check_coloring_correct(graph, coloring))
        print("Widgerson: n = 1000, p = 0.2:", max(coloring) + 1, "colors")
        graph = generate_random_graph(300, 300, 400, 0.9)
        coloring = Widgerson(graph).get_coloring()
        self.assertTrue(check_coloring_correct(graph, coloring))
        print("Widgerson: n = 1000, p = 0.9:", max(coloring) + 1, "colors")
        graph = generate_random_graph(500, 500, 500, 0.1)
        coloring = Widgerson(graph).get_coloring()
        self.assertTrue(check_coloring_correct(graph, coloring))
        print("Widgerson: n = 1500, p = 0.1:", max(coloring) + 1, "colors")
        graph = generate_random_graph(700, 700, 600, 0.05)
        coloring = Widgerson(graph).get_coloring()
        self.assertTrue(check_coloring_correct(graph, coloring))
        print("Widgerson: n = 2000, p = 0.05:", max(coloring) + 1, "colors")
        graph = generate_random_graph(1000, 1000, 1000, 0.05)
        coloring = Widgerson(graph).get_coloring()
        self.assertTrue(check_coloring_correct(graph, coloring))
        print("Widgerson: n = 3000, p = 0.05:", max(coloring), "colors")


class IntegrationBergerRompelTest(TestCase):
    def test_berger_rompel_manual(self):
        graph = [[1, 2], [0, 2], [0, 1]]
        coloring = BergerRompel(graph).get_coloring()
        self.assertTrue(check_coloring_correct(graph, coloring))
        graph = [[], [], []]
        coloring = BergerRompel(graph).get_coloring()
        self.assertTrue(check_coloring_correct(graph, coloring))
        graph = [[1], [0], [3], [2]]
        coloring = BergerRompel(graph).get_coloring()
        self.assertTrue(check_coloring_correct(graph, coloring))

    def test_berger_rompel_stress(self):
        graph = generate_random_graph(300, 300, 400, 0.5)
        coloring = BergerRompel(graph).get_coloring()
        self.assertTrue(check_coloring_correct(graph, coloring))
        print("Berger-Rompel: n = 1000, p = 0.5:", max(coloring) + 1, "colors")
        graph = generate_random_graph(300, 300, 400, 0.05)
        coloring = BergerRompel(graph).get_coloring()
        self.assertTrue(check_coloring_correct(graph, coloring))
        print("BergerRompel: n = 1000, p = 0.05:", max(coloring) + 1, "colors")
        graph = generate_random_graph(400, 300, 300, 0.1)
        coloring = BergerRompel(graph).get_coloring()
        self.assertTrue(check_coloring_correct(graph, coloring))
        print("BergerRompel: n = 1000, p = 0.1:", max(coloring) + 1, "colors")


if __name__ == '__main__':
    unittest.main()
