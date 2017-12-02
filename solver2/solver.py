import argparse
from constraint import *
import operator
import collections
import copy

"""
======================================================================
  Complete the following function.
======================================================================
"""

GRAY, BLACK = 0, 1

def checkCycle(g):
    """Return True if the directed graph g has a cycle.
    g must be represented as a dictionary mapping vertices to
    iterables of neighbouring vertices.

    For example:
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

def processConstraints(constraints):
    newConstraints = []
    

def solve(num_wizards, num_constraints, wizards, constraints):
    """
    Write your algorithm here.
    Input:
        num_wizards: Number of wizards
        num_constraints: Number of constraints
        wizards: An array of wizard names, in no particular order
        constraints: A 2D-array of constraints,
                     where constraints[0] may take the form ['A', 'B', 'C']
    Output:
        An array of wizard names in the ordering your algorithm returns
    """

    graph = {}
    branches = []
    constraintIndices = []

    for wizard in wizards:
        graph[wizard] = set()
    index = 0
    while (index < len(constraints)):
    	constraint = constraints[index]
        a = constraint[0]
        b = constraint[1]
        c = constraint[2]

        graph2 = copy.deepcopy(graph)

        graph[c].add(a)
        graph[c].add(b)
        graph2[a].add(c)
        graph2[b].add(c)

        if not checkCycle(graph2):
            branches.append(graph2)
            constraintIndices.append(index)

        if not checkCycle(graph):
            index += 1
        else:
        	graph = branches.pop()
        	index = constraintIndices.pop() + 1

    result = topological(graph)
    return list(result)

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
