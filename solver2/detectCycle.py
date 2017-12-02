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

a = set([2])
b = set()
c = set([2])
print checkCycle({1: a, 2: b, 3: c})

a = set([2])
b = set([3])
c = set([1])
print checkCycle({1: a, 2: b, 3: c})

graph3 = {
    "a": set(["b", "c", "d"]),
    "b": set([]),
    "c": set(["d", "e"]),
    "d": set([]),
    "e": set(["g", "f", "q"]),
    "g": set(["c"]),
    "f": set([]),
    "q": set([])
}

print checkCycle(graph3)
