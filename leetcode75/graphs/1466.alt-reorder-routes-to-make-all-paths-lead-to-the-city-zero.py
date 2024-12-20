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
        city_dirs = set()

        for in_city, out_city in connections:
            city_graph[in_city].append(out_city)
            city_graph[out_city].append(in_city)
            city_dirs.add((in_city, out_city))

        visited = set([0])

        def dfs(in_city: int) -> int:
            count = 0

            for out_city in city_graph[in_city]:
                if out_city in visited:
                    continue

                # count outdir
                if (in_city, out_city) in city_dirs:
                    count += 1

                visited.add(out_city)
                count += dfs(out_city)

            return count

        return dfs(0)


# @lc code=end
