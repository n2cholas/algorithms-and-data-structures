# Graph

# Undirected unweighted graph implementation

class Graph:
    def __init__(self, v):
        self.v = v
        self.e = 0
        self.adj = [set() for i in range(v)]

    def validate(self, v):
        if v is int and (v < 0 or v >= self.v):
            raise Exception
        elif v is list:
            for i in v:
                if i < 0 or i >= self.v:
                    raise Exception

    def addEdge(self, v, w):
        validate([v, w])
        self.e += 1
        self.adj[v].add(w)
        self.adj[w].add(v)

    def degree(self, v):
        validate(v)
        return len(self.adj[v])

    def adj(self, v):
        validate(v)
        return self.adj[v]
