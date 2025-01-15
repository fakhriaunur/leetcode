class UnionFind:
    def __init__(self):
        self.id = {}

    def find(self, x):
        y = self.id.get(x, x)

        if y != x:
            self.id[x] = y = self.find(y)

        return y

    def union(self, x, y):
        self.id[self.find(x)] = self.find(y)


def umbristan(n: int, breaks: list[list[int]]) -> list[int]:
    dsu = UnionFind()
    ans = []
    connected_count = n

    breaks.reverse()

    for a, b in breaks:
        ans.append(connected_count)

        if dsu.find(a) != dsu.find(b):
            dsu.union(a, b)
            connected_count -= 1

    ans.reverse()
    return ans
