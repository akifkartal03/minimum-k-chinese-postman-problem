from igraph import *
import random


# A class to to encapsulate a graph.
# It includes all necessary methods for a graph
class MyGraph:

    def __init__(self):
        self.__g = None
        self.__initial_vertex = 0

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
        while isOkey:
            print("isOkey")
            rand_edges = []
            parallel_edges = []
            degrees = [0] * number_of_vertex
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
            #if 1 in degrees:
                #isOkey = True
                #else:
                #isOkey = False
            isOkey = False
            print(degrees)
        for i in range(len(parallel_edges)):
            value = random.sample(range(0, self.__g.vcount()), 2)
            while self.is_in(value,rand_edges):
                value = random.sample(range(0, self.__g.vcount()), 2)
            rand_edges.append(value)
        """
        for x in range(0, number_of_vertex):
            if self.__g.degree(x) == 0:
                return True
            if self.__g.degree(x) == 1:
                print("akif")
                print(self.__g.degree(x))
                print(x)
                value = random.randint(0, number_of_vertex)
                while value == x or self.is_in(x, value, rand_edges):
                    value = random.randint(0, number_of_vertex)
                edge = [x, value]
                rand_edges.append(edge)
                self.__g.add_edge(x,value)
                degrees.append(self.__g.degree(x) + 1)
            else:
                degrees.append(self.__g.degree(x))

        if all(x % 2 == 0 for x in degrees):
            print("all oddd")
            index_min = min(range(len(degrees)), key=degrees.__getitem__)
            value = random.randint(0, number_of_vertex)
            while value == index_min or self.is_in(index_min, value, rand_edges):
                value = random.randint(0, number_of_vertex)
            edge = [index_min, value]
            rand_edges.append(edge)
            self.__g.add_edge(index_min, value)
        """
        print("edges:")
        print(rand_edges)
        print(len(rand_edges))
        self.__g.add_edges(rand_edges)
        rand_weights = []
        for x in range(0, len(self.__g.get_edgelist())):
            rand_weights.append(random.randint(5, 40))
        self.__g.simplify(combine_edges=None)
        self.__g.es['weight'] = rand_weights
        self.__g.es['label'] = rand_weights
        self.__g.es["curved"] = False
        return parallel_edges

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
