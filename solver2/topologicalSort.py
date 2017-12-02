# Simple:
# a --> b
#   --> c --> d
#   --> d
graph1 = {
    "a": set(["b", "c", "d"]),
    "b": set([]),
    "c": set(["d"]),
    "d": set([])
}

# 2 components
graph2 = {
    "a": set(["b", "c", "d"]),
    "b": set([]),
    "c": set(["d"]),
    "d": set([]),
    "e": set(["g", "f", "q"]),
    "g": set([]),
    "f": set([]),
    "q": set([])
}

# cycle
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

graph4 = {
    "a": ["b", "c", "d"],
    "b": [],
    "c": ["d"],
    "d": []
}

from collections import deque

GRAY, BLACK = 0, 1

def topological(graph):
    order, enter, state = deque(), set(graph), {}

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

    while enter: dfs(enter.pop())
    return order

# check how it works
print topological(graph1)
print topological(graph2)
try: topological(graph3)
except ValueError: print "Cycle!"
