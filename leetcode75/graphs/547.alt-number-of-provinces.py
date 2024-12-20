#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

from typing import List


# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city: int):
            visited.add(city)

            for neighbor in range(len(isConnected[0])):
                if isConnected[city][neighbor] == 1:
                    if neighbor in visited:
                        continue

                    dfs(neighbor)

        visited = set()
        count = 0

        for city in range(len(isConnected)):
            if city in visited:
                continue

            dfs(city)

            count += 1

        return count


# @lc code=end
