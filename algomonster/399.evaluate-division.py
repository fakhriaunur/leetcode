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
        def divide(dividend: float | str, divisor: float | str, visited) -> float:
            if dividend == divisor:
                return 1

            for new_dividend, multiplier in eq_graph[dividend]:
                if new_dividend not in visited:
                    visited.add(new_dividend)
                    ans = divide(new_dividend, divisor, visited)
                    if ans > 0:
                        return ans * multiplier
                    visited.remove(new_dividend)

            return -1

        eq_graph = defaultdict(list)
        for i, [dividend, divisor] in enumerate(equations):
            eq_graph[dividend].append((divisor, values[i]))
            eq_graph[divisor].append((dividend, 1 / values[i]))

        res = []

        for c, d in queries:
            if not eq_graph[c] or not eq_graph[d]:
                res.append(-1.0)
            else:
                visited = set()
                visited.add(c)
                res.append(divide(c, d, visited))

        return res


# @lc code=end
