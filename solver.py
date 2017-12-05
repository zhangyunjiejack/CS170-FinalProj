import argparse
from constraint import *
import operator
import collections
import copy
from numba import jit

"""
======================================================================
  Complete the following function.
======================================================================
"""

GRAY, BLACK = 0, 1

def checkCycle(g):
    """Return True if the directed graph g has a cycle.
    g must be represented as a dictionary mapping vertices to
    iterables of neighbouring vertices. For example:

    >>> cyclic({1: (2,), 2: (3,), 3: (1,)})
    True
    >>> cyclic({1: (2,), 2: (3,), 3: (4,)})
    False

    """
    path = set()
    visited = set()

    def visit(vertex):
        if vertex in visited:
            return False
        visited.add(vertex)
        path.add(vertex)
        for neighbour in g.get(vertex, ()):
            if neighbour in path or visit(neighbour):
                return True
        path.remove(vertex)
        return False

    return any(visit(v) for v in g)

def topological(graph):
    """
    Run a topological sort on the given graph so that the vertices are returned in the desired order in the form of the list. 
    """
    order = collections.deque()
    enter = set(graph)
    state = {}

    def dfs(node):
        state[node] = GRAY
        for k in graph.get(node, ()):
            sk = state.get(k, None)
            if sk == GRAY: raise ValueError("cycle")
            if sk == BLACK: continue
            enter.discard(k)
            dfs(k)
        order.appendleft(node)
        state[node] = BLACK

    while enter:
        dfs(enter.pop())
    return order


def solve(num_wizards, num_constraints, wizards, constraints):
    """
    Write your algorithm here.
    Input:
        num_wizards: Number of wizards
        num_constraints: Number of constraints
        wizards: An array of wizard names, in no particular order
        constraints: A 2D-array of constraints,
                     where constraints[0] may take the form ['A', 'B', 'C']i

    Output:
        An array of wizard names in the ordering your algorithm returns
    """

    all_graphs = []
    graph = {}
    branches = []
    constraintIndices = []

    for wizard in wizards:
    	# print(wizard)
        graph[wizard] = set()

    # all_graphs.append(graph)

    index = 0
    while (index < len(constraints)):
    	# print(str(index) + "\n")

    	constraint = constraints[index]
        a = constraint[0]
        b = constraint[1]
        c = constraint[2]

        # new_graphs = []

        # for graph in all_graphs:

        graph1 = copy.deepcopy(graph)
        graph2 = copy.deepcopy(graph)

        graph1[c].add(a)
        graph1[c].add(b)
        graph2[a].add(c)
        graph2[b].add(c)
        # new_graphs.append(graph1)
        # new_graphs.append(graph2)


        if not checkCycle(graph2):
            branches.append(graph2)
            constraintIndices.append(index)

        if not checkCycle(graph1):
            graph = graph1
            index += 1
        else:
        	graph = branches.pop()
        	index = constraintIndices.pop() + 1

    # print(all_graphs)
    result = topological(graph)
    return list(result)

    # return wizards


    # ages = []
    # resultList = []

    # for i in range(1, num_wizards + 1):
    #     ages.append(i)

    # problem = Problem()
    # wizardsAges = {}
    # for wizard in wizards:
    #     problem.addVariable(wizard, ages)

    # for constraint in constraints:
    #     problem.addConstraint(lambda a, b, c: (c < a and c < b) or (c > a and c > b), (constraint[0], constraint[1], constraint[2]))

    # resultDict = problem.getSolution()
    # sorted_tuples = sorted(resultDict.items(), key = operator.itemgetter(1))

    # for each in sorted_tuples:
    #     resultList.append(each[0])

    # return resultList


"""
======================================================================
   No need to change any code below this line
======================================================================
"""

def read_input(filename):
    with open(filename) as f:
        num_wizards = int(f.readline())
        num_constraints = int(f.readline())
        constraints = []
        wizards = set()
        for _ in range(num_constraints):
            c = f.readline().split()
            constraints.append(c)
            for w in c:
                wizards.add(w)

    wizards = list(wizards)
    return num_wizards, num_constraints, wizards, constraints

def write_output(filename, solution):
    with open(filename, "w") as f:
        for wizard in solution:
            f.write("{0} ".format(wizard))

if __name__=="__main__":
    parser = argparse.ArgumentParser(description = "Constraint Solver.")
    parser.add_argument("input_file", type=str, help = "___.in")
    parser.add_argument("output_file", type=str, help = "___.out")
    args = parser.parse_args()

    num_wizards, num_constraints, wizards, constraints = read_input(args.input_file)
    solution = solve(num_wizards, num_constraints, wizards, constraints)
    write_output(args.output_file, solution)
