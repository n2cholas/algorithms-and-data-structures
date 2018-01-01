# Max Priority Queue

class MaxPQ:
    def __init__(self):
        self.n = 0
        self.pq = [0]

    def isEmpty(self):
        return self.n

    def insert(self, x):
        self.n += 1
        self.pq.append(x)
        self.swim(self.n)

    def delMax(self):
        if not self.n:
            raise Exception("Can't delete from empty PQ")

        hi = self.pq[1]
        self.pq[1], self.pq[self.n] = self.pq[self.n], self.pq[1]
        self.n -= 1
        del self.pq[self.n+1]
        self.sink(1)
        return hi

    def swim(self, k):
        while k>1 and self.pq[k//2] < self.pq[k]:
            self.pq[k//2], self.pq[k] = self.pq[k], self.pq[k//2]
            k = k//2

    def sink(self, k):
        while 2*k <= self.n:
            j = 2*k
            if j < self.n and self.pq[j] < self.pq[j+1]:
                j += 1
            if self.pq[k] >= self.pq[j] :
                break
            self.pq[k], self.pq[j] = self.pq[j], self.pq[k]
            k = j

    def __iter__(self):
        class PQIterator:
            def __init__(s):
                s.pq = MaxPQ()
                for i in range(self.n):
                    s.pq.insert(self.pq[i])

            def __iter__(s):
                return s

            def __next__(s):
                if not s.pq.n:
                    raise StopIteration
                return s.pq.delMax()
        return PQIterator()

if __name__ == "__main__":
    pq = MaxPQ()
    x = [1, 2, -1, 5, 3, 2, 15, 4]
    for i in x:
        pq.insert(i)
    for i in pq:
        print(i)

