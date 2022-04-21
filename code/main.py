from my_graph import *


# I didn't want to bother with global variables therefore,
# I created a class to encapsulate my algorithm.
class MyAlgorithm:

    def __init__(self, my_graph):
        self.__my_graph = my_graph
        self.__sorted_edges = []
        self.__closed_walks = []
        self.__walks_lengths = []

    def my_algorithm(self, s, k):
        print("algo starts")
        self.sort_edges_descending()
        print("sorted edges:")
        print(self.__sorted_edges)
        self.create_closed_walk()
        print("walks:")
        print(self.__closed_walks)

    def sort_edges_descending(self):
        weights = self.__my_graph.get_weights()
        edges = self.__my_graph.get_edges()
        print("edges")
        print(edges)
        n = len(weights)
        for i in range(n):
            for j in range(0, n - i - 1):
                if weights[j] < weights[j + 1]:
                    edges[j], edges[j + 1] = edges[j + 1], edges[j]
                    weights[j], weights[j + 1] = weights[j + 1], weights[j]
        self.create_edge_dict(edges, weights)

    def create_edge_dict(self, edges, weights):
        n = len(weights)
        for i in range(n):
            edge = edges[i]
            my_dict = {
                'start_node': edge[0],
                'end_node': edge[1],
                'length': weights[i]
            }
            self.__sorted_edges.append(my_dict)

    def get_edge_length(self, edge):
        for e in self.__sorted_edges:
            if (e['start_node'] == edge[0] and e['end_node'] == edge[1]) or \
                    (e['start_node'] == edge[1] and e['end_node'] == edge[0]):
                return e['length']
        return 0

    def is_in_edge_list(self, edge):
        for e in self.__sorted_edges:
            if (e['start_node'] == edge[0] and e['end_node'] == edge[1]) or \
                    (e['start_node'] == edge[1] and e['end_node'] == edge[0]):
                return True
        return False

    def create_closed_walk(self):

        for e in self.__sorted_edges:

            # e = {vi, vj}
            path3 = [e['start_node'], e['end_node']]
            walk = []
            # if e is not already covered by an existing tour.
            if not self.check_added(path3):

                # SP(v1, vi)
                path1 = self.__my_graph.get_shortest_path(self.__my_graph.get_initial_vertex(), path3[0])[0]
                # SP(vj, v1)
                path2 = self.__my_graph.get_shortest_path(path3[1], self.__my_graph.get_initial_vertex())[0]



                # eğer path1 ile path2 merge olursa
                if self.try_to_merge(path1, path2, walk):
                    # path3 ile birleştirmeye çalış
                    self.add_edge_to_walk(walk, path3)
                # eğer path1 ile path3 merge olursa
                elif self.try_to_merge(path1, path3, walk):
                    # path2 ile birleştirmeye çalış
                    self.add_edge_to_walk(walk, path2)
                # eğer path2 ile path3 merge olursa
                elif self.try_to_merge(path2, path3, walk):
                    # path1 ile birleştirmeye çalış
                    self.add_edge_to_walk(walk, path1)
                else:
                    walk.extend(self.get_maximum(path1, path2, path3))
                if len(walk) > 1:
                    if walk[0] != walk[-1] and self.is_in_edge_list([walk[0],walk[-1]]):
                        walk.extend(walk[0])
                    self.__closed_walks.append({'walk': walk, 'length': self.get_walk_length(walk)})

    def get_maximum(self, a, b, c):

        if (len(a) >= len(b)) and (len(a) >= len(c)):
            largest = a

        elif (len(b) >= len(a)) and (len(b) >= len(c)):
            largest = b
        else:
            largest = c

        return largest

    def check_added(self, edge):
        for e in self.__closed_walks:
            walk = e['walk']
            if self.sub_list_exists(walk,edge):
                return True
            edge.reverse()
            if self.sub_list_exists(walk,edge):
                return True
        return False

    def sub_list_exists(self,list1, list2):
        if len(list2) < 2:
            return False
        return ''.join(map(str, list2)) in ''.join(map(str, list1))

    def try_to_merge(self, path1, path2, walk):

        if len(path1) > 1 and len(path2) > 1 and \
                (not self.check_include(path1, path2)):
            if path1[-1] == path2[0]:
                if len(walk) >= len(path1):
                    if not self.sub_list_exists(walk,path1):
                        walk.extend(path1)
                else:
                    walk.extend(path1)

                if len(walk) >= len(path2[1:]):
                    if not self.sub_list_exists(walk,path2[1:]):
                        walk.extend(path2[1:])
                else:
                    walk.extend(path2[1:])

                return True

            elif self.is_in_edge_list([path1[0], path2[-1]]):
                if len(walk) >= len(path2):
                    if not self.sub_list_exists(walk,path2):
                        walk.extend(path2)
                else:
                    walk.extend(path2)

                if len(walk) >= len(path1):
                    if not self.sub_list_exists(walk,path1):
                        walk.extend(path1)
                else:
                    walk.extend(path1)

                return True

            elif self.is_in_edge_list([path1[-1], path2[0]]):
                if len(walk) >= len(path1):
                    if not self.sub_list_exists(walk,path1):
                        walk.extend(path1)
                else:
                    walk.extend(path1)

                if len(walk) >= len(path2):
                    if not self.sub_list_exists(walk,path2):
                        walk.extend(path2)
                else:
                    walk.extend(path2)

                return True
            elif path1[0] == path2[-1]:
                if len(walk) >= len(path2):
                    if not self.sub_list_exists(walk,path2):
                        walk.extend(path2)
                else:
                    walk.extend(path2)

                if len(walk) >= len(path1[1:]):
                    if not self.sub_list_exists(walk,path1[1:]):
                        walk.extend(path1[1:])
                else:
                    walk.extend(path1[1:])
                return True

            else:
                return False
        else:
            return False

    def add_edge_to_walk(self, walk, path3):
        # walk eğer path'ü içermiyorsa path3'u ekle
        if len(walk) > 1 and len(path3) > 1 and \
                (not self.check_include(walk, path3)):
            # eğer path1'in son node'u ile path3'un ilk node'u eşitse
            if walk[-1] == path3[0]:
                if len(walk) >= len(path3[1:]):
                    if not self.sub_list_exists(walk,path3[1:]):
                        walk.extend(path3[1:])
                else:
                    walk.extend(path3[1:])


            elif self.is_in_edge_list([walk[-1], path3[0]]):
                if len(walk) >= len(path3):
                    if not self.sub_list_exists(walk,path3):
                        walk.extend(path3)
                else:
                    walk.extend(path3)

            elif self.is_in_edge_list([walk[0], path3[-1]]):
                if len(path3) >= len(walk):
                    if not self.sub_list_exists(path3,walk):
                        path3.extend(walk)
                else:
                    path3.extend(walk)

            elif walk[0] == path3[-1]:

                if len(path3) >= len(walk[1:]):
                    if not self.sub_list_exists(path3,walk[1:]):
                        path3.extend(walk[1:])
                else:
                    path3.extend(walk[1:])

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

    def get_walk_length(self, walk):
        if len(walk) > 0:
            # Add up the weights across all edges on the shortest path
            distance = 0
            n = len(walk)
            for i in range(0, n):
                if i + 1 != n:
                    edge = [walk[i], walk[i + 1]]
                    distance += self.get_edge_length(edge)
            return distance
        else:
            print("walk is empty")
            return 0


graph = MyGraph()
graph.generate_random_graph(5, 10, 0)
graph.print_graph(4)
alg = MyAlgorithm(graph)
alg.my_algorithm(5, 4)
# print(alg.check_include([4, 3, 1, 0], [3, 4]))
