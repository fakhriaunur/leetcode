#
# @lc app=leetcode id=1466 lang=python3
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#

from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        city_graph: defaultdict[int, list[int]] = defaultdict(list)
        orig_connections: set[tuple[int, int]] = set()

        for a, b in connections:
            city_graph[a].append(b)
            city_graph[b].append(a)
            orig_connections.add((a, b))

        visited = set()

        def dfs(orig: int) -> int:
            visited.add(orig)
            count = 0

            for dest in city_graph[orig]:
                if dest not in visited:
                    if (orig, dest) in orig_connections:
                        count += 1

                    count += dfs(dest)

            return count

        return dfs(0)


# @lc code=end
