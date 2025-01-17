from typing import List


def min_cost_to_visit_every_node(graph: List[List[int]]) -> int:
    MAX = float("inf")
    n = len(graph)
    dp = [[0] * n for _ in range(1 << n)]

    def f(bitmask, curr):
        if bitmask == (1 << n) - 1:
            return 0

        if dp[bitmask][curr] != 0:
            return dp[bitmask][curr]

        res = MAX

        # loop thru all neighbors for this current node
        for i in range(len(graph[curr])):
            if (bitmask & (1 << i)) == 0 and graph[curr][i] != 0:
                res = min(res, graph[curr][i] + f(bitmask | (1 << i), i))

        dp[bitmask][curr] = res
        return res

    ans = f(1, 0)
    return -1 if ans == MAX else int(ans)


if __name__ == "__main__":
    graph = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = min_cost_to_visit_every_node(graph)
    print(res)
