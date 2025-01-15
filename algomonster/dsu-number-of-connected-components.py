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


def number_of_connected_components(n: int, connections: list[list[int]]) -> list[int]:
    dsu = UnionFind()
    ans = []
    connected_count = n

    for a, b in connections:
        if dsu.find(a) != dsu.find(b):
            dsu.union(a, b)
            connected_count -= 1

        ans.append(connected_count)

    return ans
