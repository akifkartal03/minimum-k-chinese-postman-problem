
initial_vertex = 0
graph = []
cycles = []
k=0
found = []

def main(edges,init_vertex,k_value):
    global graph
    global cycles
    global initial_vertex
    global k
    global found
    k = k_value
    initial_vertex = init_vertex
    graph = map(list, edges)
    #graph = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 4], [1, 5], [2, 3], [2, 5], [4, 5]]
    print(k)
    print(init_vertex)
    print(graph)
    for edge in graph:
        for node in edge:
            findNewCycles([node])
    for cy in cycles:
        cy.append(cy[0])
    print(cycles)
    n = len(cycles)
    printCombination(cycles, n, k)
    print(found)
    return found

def findNewCycles(path):
    start_node = path[0]
    next_node = None
    sub = []

    # visit each edge and each node of each edge
    for edge in graph:
        node1, node2 = edge
        if start_node in edge:
            if node1 == start_node:
                next_node = node2
            else:
                next_node = node1
            if not visited(next_node, path):
                # neighbor node not on path yet
                sub = [next_node]
                sub.extend(path)
                # explore extended path
                findNewCycles(sub)
            elif len(path) > 2 and next_node == path[-1]:
                # cycle found
                p = rotate_to_smallest(path)
                inv = invert(p)
                if isNew(p) and isNew(inv):
                    cycles.append(p)


def invert(path):
    return rotate_to_smallest(path[::-1])


#  rotate cycle path such that it begins with the smallest node
def rotate_to_smallest(path):
    n = path.index(min(path))
    return path[n:] + path[:n]


def isNew(path):
    return not path in cycles


def visited(node, path):
    return node in path


# Program to print all combination
# of size r in an array of size n

# The main function that prints
# all combinations of size r in
# arr[] of size n. This function
# mainly uses combinationUtil()
def printCombination(arr, n, r):
    # A temporary array to
    # store all combination
    # one by one
    data = [0] * r

    # Print all combination
    # using temporary array 'data[]'
    combinationUtil(arr, data, 0,
                    n - 1, 0, r)


# arr[] ---> Input Array
# data[] ---> Temporary array to
#		 store current combination
# start & end ---> Starting and Ending
#			 indexes in arr[]
# index ---> Current index in data[]
# r ---> Size of a combination
# to be printed
def combinationUtil(arr, data, start,
                    end, index, r):
    # Current combination is ready
    # to be printed, print it
    if (index == r):
        findMatch(data)
        return

    # replace index with all
    # possible elements. The
    # condition "end-i+1 >=
    # r-index" makes sure that
    # including one element at
    # index will make a combination
    # with remaining elements at
    # remaining positions
    i = start
    while (i <= end and end - i + 1 >= r - index):
        data[index] = arr[i]
        combinationUtil(arr, data, i + 1,
                        end, index + 1, r)
        i += 1

def findMatch(cycle):
    if checkInitialVertex(cycle):
        found.append(cycle)
        return True
    else:
        return False

def checkInitialVertex(cycle):
    lst = [0] * len(graph)
    for e in cycle:
        if initial_vertex in e:
            i = 0
            for edg in graph:
                if check_added2(e,edg):
                    lst[i] = 1
                i = i + 1
        else:
            return False
    if 0 in lst:
        return False
    return True

def check_added2(cycle, edge):
    if sub_list_exists(cycle, edge):
        return True
    edge.reverse()
    if sub_list_exists(cycle, edge):
        return True
    return False

def sub_list_exists(list1, list2):
    if len(list2) < 2:
        return False
    return ''.join(map(str, list2)) in ''.join(map(str, list1))
"""
arr = [1, 2, 3, 4, 5]
r = 3
n = len(arr)
printCombination(arr, n, r)
"""

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

#main(0,0,3)