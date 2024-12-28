#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

from collections import deque
from typing import List


# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        n = len(grid)
        entry = 0, 0
        queue = deque([entry])
        grid[0][0] = 1
        # visited = set([entry])

        path_length = 1

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()

                if x == y == n - 1:
                    return path_length

                for nx in range(max(0, x - 1), min(n, x + 2)):
                    for ny in range(max(0, y - 1), min(n, y + 2)):
                        if grid[nx][ny] == 0:
                            grid[nx][ny] = 1
                            queue.append((nx, ny))

                        # if (nx, ny) not in visited and grid[nx][ny] == 0:
                        #     visited.add((nx, ny))
                        #     queue.append((nx, ny))

            path_length += 1

        return -1


# @lc code=end
