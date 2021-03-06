# I didn't want to bother with global variables therefore,
# I created a class to encapsulate my simple exhausted search algorithm.
class MySimpleAlgorithm:

    def __init__(self, edges, init_vertex, k_value, node, cyc):
        self.graph = [list(elem) for elem in edges]
        self.cycles = cyc
        self.found = []
        self.initial_vertex = init_vertex
        self.k = k_value
        self.n = node

    def main(self):
        print(self.k)
        print(self.initial_vertex)

        print(self.graph)
        print(len(self.graph))
        print(self.cycles)
        start = len(self.cycles)

        for edge in self.graph:
            for node in edge:
                self.findNewCycles([node])

        self.cycles = [x for x in self.cycles if not self.determine(x)]
        for i in range(start, len(self.cycles)):
            cyc = self.cycles[i]
            cyc.append(cyc[0])

        while len(self.cycles) <= self.k:
            adj = self.get_adj(self.initial_vertex)
            for e in adj:
                lst = [self.initial_vertex, e, self.initial_vertex]
                self.cycles.append(lst)

        print(len(self.cycles))
        self.findCombinations(self.cycles, self.k)
        return self.found

    def determine(self, cylce):
        if self.initial_vertex not in cylce:
            return True
        return False

    def get_adj(self, node):
        new_edges = []
        for edge in self.graph:
            if node in edge:
                temp = [edge[0], edge[1]]
                temp.remove(node)
                new_edges.append(temp[0])
        return new_edges

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
                                    n - 1, 0, r, rate)

    def combinationUtil(self, arr, data, start,
                        end, index, r, rates):
        if index == r:
            rates.append(data)
            return
        i = start
        while i <= end and end - i + 1 >= r - index:
            data[index] = arr[i]
            self.combinationUtil(arr, data, i + 1,
                                 end, index + 1, r, rates)
            i += 1
        return rates

    def findMatch(self, cycle):
        if self.checkConditions(cycle):
            self.found.append(cycle)
            return True
        else:
            return False

    def checkConditions(self, cycle):
        lst = [0] * len(self.graph)
        for e in cycle:
            i = 0
            for edg in self.graph:
                if self.check_added2(e, edg):
                    lst[i] = 1
                i = i + 1
        if 0 in lst:
            return False
        return True

    def check_added2(self, cycle, edge):
        if self.sub_list_exists(cycle, edge):
            return True
        temp_edge = [edge[1], edge[0]]
        if self.sub_list_exists(cycle, temp_edge):
            return True
        return False

    def sub_list_exists(self, list1, list2):
        if len(list2) < 2:
            return False
        return ''.join(map(str, list2)) in ''.join(map(str, list1))

    def findCombinations(self, A, k, out=(), i=0):

        # invalid input
        if len(A) == 0 or k > len(A):
            return

        # base case: combination size is `k`
        if k == 0:
            # check problem conditions
            self.findMatch(out)
            return

        # start from the next index till the last index
        for j in range(i, len(A)):
            # add current element `A[j]` to the solution and recur for next index
            # `j+1` with one less element `k-1`
            self.findCombinations(A, k - 1, out + (A[j],), j + 1)

