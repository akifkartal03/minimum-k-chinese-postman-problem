from igraph import *
import random


# A class to to encapsulate a graph.
# It includes all necessary methods for a graph
class MyGraph:

    def __init__(self):
        self.__g = None
        self.__initial_vertex = 0
        self.__r_edges = []
        self.__is1degree = False
        self.__degree1 = []

    def generate_random_graph(self, number_of_vertex, number_of_edges, initial_vertex):
        self.__initial_vertex = initial_vertex
        self.__g = Graph()
        self.__g.add_vertices(number_of_vertex)

        for i in range(len(self.__g.vs)):
            self.__g.vs[i]["id"] = i
            self.__g.vs[i]["label"] = i

        rand_edges = []
        parallel_edges = []
        isOkey = True
        degrees = [0] * number_of_vertex
        while isOkey:
            print("isOkey")
            rand_edges = []
            parallel_edges = []
            for x in range(0, number_of_edges):
                value = random.sample(range(0, self.__g.vcount()), 2)
                while value in rand_edges:
                    value = random.sample(range(0, self.__g.vcount()), 2)
                temp_val = [value[1], value[0]]
                if temp_val in rand_edges:
                    parallel_edges.append(temp_val)
                else:
                    for node in value:
                        degrees[node] = degrees[node] + 1
                rand_edges.append(value)
            if degrees[initial_vertex] == 0:
                isOkey = True
            else:
                isOkey = False
            print(degrees)
        for i in range(len(parallel_edges)):
            value = random.sample(range(0, self.__g.vcount()), 2)
            while self.is_in(value, rand_edges):
                value = random.sample(range(0, self.__g.vcount()), 2)
            rand_edges.append(value)

        print("edges:")
        print(rand_edges)
        print(len(rand_edges))
        self.__r_edges = rand_edges
        self.__g.add_edges(rand_edges)
        rand_weights = []
        for x in range(0, len(self.__g.get_edgelist())):
            rand_weights.append(random.randint(5, 40))
        self.__g.simplify(combine_edges=None)
        self.__g.es['weight'] = rand_weights
        self.__g.es['label'] = rand_weights
        self.__g.es["curved"] = False
        degrees2 = [0] * number_of_vertex
        for i in range(number_of_vertex):
            degrees2[i] = self.__g.degree(i)
            if degrees2[i] == 1:
                self.__is1degree = True
                graf = self.get_edges()
                adj = self.get_adj(i,graf)
                lst = (i, adj[0])
                lst2 = [i, adj[0]]
                if lst in graf:
                    self.__degree1.append(lst2)
                else:
                    lst2.reverse()
                    self.__degree1.append(lst2)
        print("degre2")
        print(degrees2)
        return parallel_edges

    def get_adj(self, node, graf):
        new_edges = []
        for edge in graf:
            if node in edge:
                temp = [edge[0], edge[1]]
                temp.remove(node)
                new_edges.append(temp[0])
        return new_edges

    def is_in(self, value, edges):
        if value in edges:
            return True
        temp_val = [value[1], value[0]]
        if temp_val in edges:
            return True
        return False

    def print_graph(self, graph_number):
        visual_style = {}

        out_name = "outputs/demo" + str(graph_number) + ".png"

        visual_style["bbox"] = (400, 400)
        visual_style["margin"] = 27

        visual_style["vertex_color"] = 'white'

        visual_style["vertex_size"] = 45

        visual_style["vertex_label_size"] = 22

        visual_style["edge_curved"] = False

        my_layout = self.__g.layout_lgl()
        visual_style["layout"] = my_layout

        plot(self.__g, out_name, **visual_style)

    def get_edges(self):
        return self.__g.get_edgelist()

    def get_edges2(self):
        return self.__r_edges

    def get_is1Degree(self):
        return self.__is1degree

    def get_degree1(self):
        return self.__degree1

    def get_initial_vertex(self):
        return self.__initial_vertex

    def get_graph(self):
        return self.__g

    def get_weights(self):
        return self.__g.es['weight']

    def print_info(self):
        print("----------Information-----------")
        print("Number of vertices in the graph:", self.__g.vcount())
        print("Number of edges in the graph", self.__g.ecount())
        print("Is the graph directed:", self.__g.is_directed())
        print("Maximum degree in the graph:", self.__g.maxdegree())
        print("Adjacency matrix:\n", self.__g.get_adjacency())
        print("weights:", self.__g.es['weight'])

    def get_shortest_path(self, start_node, destination_node):
        return self.__g.get_shortest_paths(
            start_node,
            to=destination_node,
            weights=self.__g.es["weight"],
            output="vpath",
        )

    def get_shortest_path_length(self, path):
        if len(path[0]) > 0:
            # Add up the weights across all edges on the shortest path
            distance = 0
            n = len(path[0])
            for i in range(0, n):
                if i + 1 != n:
                    mytuple = (path[0][i], path[0][i + 1])
                    distance += self.get_weight_by_index(self.get_edges().index(mytuple))
            return distance
        else:
            print("shortest path is empty")
            return 0

    def get_weight_by_index(self, index):
        return (self.__g.es["weight"])[index]


"""
graph = MyGraph()
graph.generate_random_graph(5, 10,0)
graph.print_graph(2)
path=graph.get_shortest_path(0,4)
print(path[0])
print(graph.get_edges())
print(graph.get_shortest_path_length(path))
"""
