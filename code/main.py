from my_graph import *


# I didn't want to bother with global variables therefore,
# I created a class to encapsulate my algorithm.
class MyAlgorithm:

    def __init__(self, my_graph):
        self.__my_graph = my_graph
        self.__sorted_edges = None
        self.__closed_walks = []
        self.__walks_lengths = []

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

    def create_closed_walk(self):
        added_edges = []
        temp_added = []
        for e in self.__sorted_edges:
            if list(e) not in added_edges:
                path1 = self.__my_graph.get_shortest_path(self.__my_graph.get_initial_vertex(), e[0])[0]
                path2 = self.__my_graph.get_shortest_path(e[1], self.__my_graph.get_initial_vertex())[0]
                path3 = list(e)
                walk = []
                if len(path1) > 1 and len(path2) > 1:
                    if path1[-1] == path2[0]:
                        temp = path1
                        temp.append(path2[1:])
                        if not self.check_include(temp, path3):
                            print("test")
                    print(path1)
                    print(path2)
                    print(path3)

    def add_reverse_edges(self, edge_list):
        reverse_list = []
        for e in edge_list:
            reverse_list.append(e.reverse())
        for e in reverse_list:
            edge_list.append(e)

    def check_include(self, walk, edge):
        n = len(walk)
        for i in range(0, n):
            if i + 1 != n:
                mylist = [walk[i], walk[i + 1]]
                if mylist == edge:
                    return True
                mylist.reverse()
                if mylist == edge:
                    return True
        return False


graph = MyGraph()
graph.generate_random_graph(5, 10, 0)
# graph.print_graph(2)
alg = MyAlgorithm(graph)
# alg.sort_edges_descending()
# alg.create_closed_walk()
# print(alg.check_include([4, 3, 1, 0], [3, 4]))
