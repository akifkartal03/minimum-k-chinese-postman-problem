from igraph import *
import random
import numpy as np


# Abstract representation of a graph.
class MyGraph:

    def __init__(self):
        self.__g = None

    def generate_random_graph(self, number_of_vertex, number_of_edges):
        self.__g = Graph()
        self.__g.add_vertices(number_of_vertex)
        # Add ids and labels to vertices
        for i in range(len(self.__g.vs)):
            self.__g.vs[i]["id"] = i
            self.__g.vs[i]["label"] = i

        rand_edges = []
        for x in range(0, number_of_edges):
            value = random.sample(range(0, self.__g.vcount()), 2)
            if value not in rand_edges:
                rand_edges.append(value)
        print(rand_edges)
        self.__g.add_edges(rand_edges)
        rand_weights = []
        for x in range(0, len(rand_edges)):
            rand_weights.append(random.randint(5, 40))
        print(rand_weights)
        print(len(rand_edges))
        print(len(rand_weights))
        self.__g.simplify(multiple=True, loops=False, combine_edges=None)
        self.__g.es['weight'] = rand_weights
        self.__g.es['label'] = rand_weights
        self.__g.es["curved"] = False

        print("-------summary-----")
        summary(self.__g)
        print("-----edge list------")
        print()

        # plot(self.__g)

    def print_graph(self, graph_number):
        visual_style = {}

        out_name = "outputs/graph" + str(graph_number) + ".png"

        # Set bbox and margin
        visual_style["bbox"] = (400, 400)
        visual_style["margin"] = 27

        # Set vertex colours
        visual_style["vertex_color"] = 'white'

        # Set vertex size
        visual_style["vertex_size"] = 45

        # Set vertex lable size
        visual_style["vertex_label_size"] = 22

        # Don't curve the edges
        visual_style["edge_curved"] = False

        # Set the layout
        my_layout = self.__g.layout_lgl()
        visual_style["layout"] = my_layout

        # Plot the graph
        plot(self.__g, out_name, **visual_style)

    def get_edges(self):
        return self.__g.get_edgelist()

    def print_info(self):
        print("----------Information-----------")
        print("Number of vertices in the graph:", self.__g.vcount())
        print("Number of edges in the graph", self.__g.ecount())
        print("Is the graph directed:", self.__g.is_directed())
        print("Maximum degree in the graph:", self.__g.maxdegree())
        print("Adjacency matrix:\n", self.__g.get_adjacency())
        print("The shortest paths from vertex 0 to vertex 4:", self.__g.get_shortest_paths(0, to=4))


graph = MyGraph()
graph.generate_random_graph(5, 10)
graph.print_graph(1)
graph.print_info()
