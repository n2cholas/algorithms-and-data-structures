# Directed Weighted Digraph
# includes directed edge

class DirectedGraph:
    def __init__(self, v, w, weight):
        if v<0 or w<0:
            raise Exception

        self.v = v
        self.w = w
        self.weight = weight
        
    def fro(self):
        return self.v
    def to(self):
        return self.w
    def weight(self):
        return self.weight

class WeightedDigraph:
    def __init__(self, v):
        if v < 0:
            raise Exception
        self.v = v
        self.e = 0
        self.indegree = [0]*v
        self.adj = [set() for i in range(v)]

    def validate(self, v):
        if v is int and (v < 0 or v >= self.v):
            raise Exception
        elif v is list:
            for i in range(self.v):
                if i < 0 or i >= self.v:
                    raise Exception

    def addEdge(self, e):
        v = e.fro()
        w = e.to()
        validate([v,w])
        self.adj[v].add(e)
        self.indegree[w] += 1
        self.e += 1

    def adj(self, v):
        validate(v)
        return self.adj[v]

    def outdegree(self, v):
        validate(v)
        return len(self.adj[v])

    def indegree(self,  v):
        validate(v)
        return self.indegree[v]
