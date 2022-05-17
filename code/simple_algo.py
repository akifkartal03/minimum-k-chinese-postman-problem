# I didn't want to bother with global variables therefore,
# I created a class to encapsulate my simple algorithm.

#todo
#cycle da initial vertex sayısı k dan az veya eşitşe kendin cycle eklee

#simple algoritmada graph'ın cycle üretemediği durumları kontrol et ve cycler ekle...
#kendi algoritmanda olduğu gibi
#sonra test et ve biraz kendi alogritmanı toparla
#özellikle k'dan fazla cycle üretme durumuna bidaha bak
import itertools
class MySimpleAlgorithm:

    def __init__(self, edges, init_vertex, k_value):
        self.graph = [list(elem) for elem in edges]
        #elf.graph = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 4], [1, 5], [2, 3], [2, 5], [4, 5]]
        self.cycles = []
        self.found = []

        self.initial_vertex = init_vertex
        self.k = k_value

    def main(self):
        print(self.k)
        print(self.initial_vertex)
        new_edges = []
        for edge in self.graph:
            if self.initial_vertex in edge:
                new_edges.append([edge[1],edge[0]])
        self.graph.extend(new_edges)
        print(self.graph)
        for edge in self.graph:
            for node in edge:
                self.findNewCycles([node])
        for cy in self.cycles:
            cy.append(cy[0])
        print(self.cycles)
        allPossibilities = list(itertools.combinations(self.cycles, self.k))
        for a in allPossibilities:
            self.findMatch(a)
        return self.found

    def findNewCycles(self, path):
        start_node = path[0]
        next_node = None
        sub = []

        # visit each edge and each node of each edge
        for edge in self.graph:
            node1, node2 = edge
            if start_node in edge:
                if node1 == start_node:
                    next_node = node2
                else:
                    next_node = node1
                if not self.visited(next_node, path):
                    # neighbor node not on path yet
                    sub = [next_node]
                    sub.extend(path)
                    # explore extended path
                    self.findNewCycles(sub)
                elif len(path) > 2 and next_node == path[-1]:
                    # cycle found
                    p = self.rotate_to_smallest(path)
                    inv = self.invert(p)
                    if self.isNew(p) and self.isNew(inv):
                        self.cycles.append(p)

    def invert(self, path):
        return self.rotate_to_smallest(path[::-1])

    #  rotate cycle path such that it begins with the smallest node
    def rotate_to_smallest(self, path):
        n = path.index(min(path))
        return path[n:] + path[:n]

    def isNew(self, path):
        return not path in self.cycles

    def visited(self, node, path):
        return node in path

    def printCombination(self, arr, n, r):
        # A temporary array to
        # store all combination
        # one by one
        data = [0] * r

        # Print all combination
        # using temporary array 'data[]'
        rate = []
        return self.combinationUtil(arr, data, 0,
                             n - 1, 0, r,rate)

    def combinationUtil(self, arr, data, start,
                        end, index, r,rates):
        if index == r:
            rates.append(data)
            return
        i = start
        while i <= end and end - i + 1 >= r - index:
            data[index] = arr[i]
            self.combinationUtil(arr, data, i + 1,
                                 end, index + 1, r,rates)
            i += 1
        return rates

    def findMatch(self,cycle):
        if self.checkInitialVertex(cycle):
            self.found.append(cycle)

            return True
        else:
            return False


    def checkInitialVertex(self,cycle):
        lst = [0] * len(self.graph)
        for e in cycle:
            if self.initial_vertex in e:
                i = 0
                for edg in self.graph:
                    if self.check_added2(e, edg):
                        lst[i] = 1
                    i = i + 1
            else:
                return False
        if 0 in lst:
            return False
        return True


    def check_added2(self,cycle, edge):
        if self.sub_list_exists(cycle, edge):
            return True
        edge.reverse()
        if self.sub_list_exists(cycle, edge):
            return True
        return False


    def sub_list_exists(self,list1, list2):
        if len(list2) < 2:
            return False
        return ''.join(map(str, list2)) in ''.join(map(str, list1))


"""
arr = [1, 2, 3, 4, 5]
r = 3
n = len(arr)
printCombination(arr, n, r)


def main2():
    global graph
    global cycles
    global initial_vertex
    global k
    global found
    k = 3
    graph = [[0,1],[0,2],[0,3],[0,4],[1,4],[1,5],[2,3],[2,5],[4,5]]
    data = [[0, 4, 1,0], [0, 2, 5, 4, 1,0], [0, 3, 2, 5, 4, 1,0]]
    findMatch(data)
"""
# main(0,0,3)
#algo = MySimpleAlgorithm(0,0,4)
#algo.main()