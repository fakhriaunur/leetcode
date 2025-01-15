class UnionFind:
    def __init__(self) -> None:
        self.id = {}

    def find(self, x) -> int:
        y = self.id.get(x, x)

        if y != x:
            self.id[x] = y = self.find(y)

        return y

    def union(self, x, y):
        self.id[self.find(x)] = self.find(y)


class MergeSet:
    def __init__(self) -> None:
        self.dsu = UnionFind()

    def merge(self, x, y):
        self.dsu.union(x, y)

    def is_same(self, x, y) -> bool:
        return self.dsu.find(x) == self.dsu.find(y)
