
class UnionFindHardCodedArray:
    def __init__(self, size):
        # Initially, every node is its own parent
        self.parent = [i for i in range(size)]

    def find(self, x):
        # Follow the parent chain until we reach the root
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, x, y):
        # Find roots of both elements
        rootX = self.find(x)
        rootY = self.find(y)

        # If they have different roots, merge them
        if rootX != rootY:
            self.parent[rootY] = rootX  # Attach y's root under x's root

class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        # Initialize if x is not yet in any group
        if x not in self.parent:
            self.parent[x] = x
        # Just follow the parent (no compression)
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, x, y):
        # Get roots of both elements
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.parent[rootY] = rootX  # Merge y into x's group

class UnionFindPathCompression:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.parent[rootY] = rootX

class UnionFindPathCompressionUnionByFind:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x     # Initialize as its own parent
            self.size[x] = 1       # Size of its own group is 1
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return  # Already connected
        # Union by size
        if self.size[rootX] < self.size[rootY]:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]
        else:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
