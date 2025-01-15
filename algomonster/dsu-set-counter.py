class UnionFind:
    def __init__(self):
        self.id = {}

    def find(self, x) -> int:
        y = self.id.get(x, x)

        if y != x:
            self.id[x] = y = self.find(y)

        return y

    def union(self, x, y):
        self.id[self.find(x)] = self.find(y)


class SetCounter:
    def __init__(self):
        self.dsu = UnionFind()
        self.size: dict[int, int] = {}

    def merge(self, x, y):
        if self.dsu.find(x) != self.dsu.find(y):
            new_size = self.count(x) + self.count(y)
            self.size[self.dsu.find(x)] = new_size

    def count(self, x) -> int:
        return self.size.get(self.dsu.find(x), 1)
