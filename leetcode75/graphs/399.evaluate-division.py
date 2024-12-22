#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        def find(x):
            if parent[x] != x:
                orig_parent = parent[x]
                parent[x] = find(parent[x])
                weight[x] *= weight[orig_parent]

            return parent[x]

        weight = defaultdict(lambda: 1.0)
        parent = defaultdict(str)

        for a, b in equations:
            parent[a], parent[b] = a, b

        for i, value in enumerate(values):
            a, b = equations[i]
            root_a, root_b = find(a), find(b)

            if root_a != root_b:
                parent[root_a] = root_b
                weight[root_a] = weight[b] / weight[a] * value

        results = []

        for c, d in queries:
            if c not in parent or d not in parent or find(c) != find(d):
                results.append(-1.0)
            else:
                results.append(weight[c] / weight[d])

        return results


# @lc code=end
