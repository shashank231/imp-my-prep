from pprint import pprint
from collections import deque

class Graph:
    def __init__(self, relations = dict()):
        self.relations = relations

    def addEdge(self, u, v, directed: bool = True):
        u_present = self.relations.get(u)
        if u_present:
            u_present.append(v)
        else:
            self.relations.update({u: [v]})
        if not directed:
            v_present = self.relations.get(v)
            if v_present:
                v_present.append(u)
            else:
                self.relations.update({v: [u]})

    def printAdjList(self):
        pprint(self.relations)

    def allNodes(self):
        set1 = set()
        for i in self.relations.keys():
            set1.add(i)
            for j in self.relations.get(i):
                set1.add(j)
        return list(set1)


def dfs(graph, start):
    visited = set()
    traversal = []

    def helper(node):
        if node in visited:
            return
        visited.add(node)
        traversal.append(node)
        for neighbor in graph.get(node, []):
            helper(neighbor)

    helper(start)
    return traversal


def bfs(graph, start):
    traversal = []
    visited = set()
    queue = deque()
    queue.append(start)  # queue mein dala      |
    visited.add(start)   # visited mark kiya    |

    while queue:
        node = queue.popleft()
        traversal.append(node)  # TRAVERSAL
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                queue.append(neighbour)  # queue mein dala    |
                visited.add(neighbour)   # visited mark kiya  |

    return traversal


def has_cycle_directed(graph):
    visited = set()     # Tracks ALL nodes visited across DFS runs
    rec_stack = set()   # Tracks nodes currently on the recursion path

    def dfs(node):
        if node in rec_stack:
            return True  # Cycle detected
        if node in visited:
            return False  # Already processed, no cycle from here

        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return True

        rec_stack.remove(node)  # Backtrack
        return False  # we're done exploring this path

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False


def has_cycle_undirected(graph):
    visited = set()

    def dfs(node, parent):
        if node in visited:
            return False

        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor in visited:
                if neighbor != parent:
                    return True  # ✅ Cycle found
            else:
                if dfs(neighbor, node):
                    return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True

    return False


def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph.get(node, []):
            dfs(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]



g1 = Graph()
g1.addEdge(1, 2)
g1.addEdge(1, 3)
g1.addEdge(2, 3)
g1.addEdge(2, 4)
g1.addEdge(3, 4)
g1.addEdge(4, 3)
g1.addEdge(4, 5)


# c1 = dfs(g1.relations, 1)
# print(c1)

bfs(g1.relations, 1)




















