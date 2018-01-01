# Union Find algorithm
# Includes weighted quick find, path compression
# From Algorithms, Part 1 by Princeton University

# Allows you to connect nodes and check for connectivity in lg*N time

# Time Complexity: O(N) to initialize, O(lg*N) for union and find
# Space Complexity: N

class UnionFind:
    # n is the number of sites
    def __init__ (self, n):
        self._count = n     # number of connected components
        self._parent = [i for i in range(n)] #parent[i] is the parent of i
        self._rank = [0]*n; # rank[i] is the rank of subtree rooted at i (< 31)

    # Getter method for count
    def count(self):
        return self._count;

    # Returns the ID of the common component containing site
    def find(self, p):
        self.validate(p)
        while p != self._parent[p]:
            self._parent[p] = self._parent[self._parent[p]] #compresses path on each find operation
            p = self._parent[p]
        return p

    # Ensures that p is a valid index
    def validate(self, p):
        n = len(self._parent)
        if p < 0 or p >= n:
            raise ValueError()

    # Checks if components p and q are connected
    def connected(self, p, q):
        return self.find(p) == self.find(q)

    # Merges the sites containing p and q
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return

        #make the smaller root point to the larger root
        if self._rank[rootP] < self._rank[rootQ]:
            self._parent[rootP] = rootQ
        elif self._rank[rootP] > self._rank[rootQ]:
            self._parent[rootQ] = rootP;
        else:
            self._parent[rootQ] = rootP
            self._rank[rootP] += 1 #rank goes down because it is no longer a root
            
        self._count  -= 1

# test
if __name__ == '__main__':
    uf = UnionFind(5)
    print("yo")
    print(uf.connected(1, 2))
    uf.union(1, 2)
    print(uf.connected(1, 2))
