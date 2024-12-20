#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city: int):
            visited.add(city)

            for neighbor in city_graph[city]:
                if neighbor in visited:
                    continue

                dfs(neighbor)

        city_graph = defaultdict(list)

        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    city_graph[i].append(j)

        visited = set()
        count = 0

        for i in range(len(city_graph)):
            if i in visited:
                continue

            dfs(i)

            count += 1

        return count


# @lc code=end
