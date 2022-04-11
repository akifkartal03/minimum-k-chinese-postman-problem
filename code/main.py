from my_graph import *


# I didn't want to bother with global variables therefore,
# I created a class to encapsulate my algorithm.
class MyAlgorithm:

    def __init__(self, my_graph):
        self.__my_graph = my_graph
        self.__sorted_edges = None
        self._closed_walks = None

    def my_algorithm(self, s, k):
        print("algo")

    def sort_edges_descending(self):
        weights = self.__my_graph.get_weights()
        self.__sorted_edges = self.__my_graph.get_edges()
        print(weights)
        print(self.__sorted_edges)
        n = len(weights)
        for i in range(n):
            for j in range(0, n - i - 1):
                if weights[j] < weights[j + 1]:
                    self.__sorted_edges[j], self.__sorted_edges[j + 1] = \
                        self.__sorted_edges[j + 1], self.__sorted_edges[j]
                    weights[j], weights[j + 1] = weights[j + 1], weights[j]
        print("sorted:")
        print(self.__sorted_edges)

    def create_closed_walk(self):
        print("sorted:")



graph = MyGraph()
graph.generate_random_graph(5, 10)
graph.print_graph(2)
alg = MyAlgorithm(graph)
alg.sort_edges_descending()
