#
# @lc app=leetcode id=1926 lang=python3
#
# [1926] Nearest Exit from Entrance in Maze
#

from collections import deque
from itertools import pairwise
from typing import List


# @lc code=start
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def get_neighbors(coord: tuple[int, int]) -> List[tuple[int, int]]:
            neighbors = []
            row, col = coord
            dirs = pairwise([-1, 0, 1, 0, -1])

            for dir in dirs:
                d_row, d_col = dir
                n_row = row + d_row
                n_col = col + d_col

                if 0 <= n_row < m and 0 <= n_col < n:
                    neighbors.append((n_row, n_col))

            return neighbors

        steps = 0
        m, n = len(maze), len(maze[0])
        row, col = entrance
        queue = deque([(row, col)])
        maze[row][col] = "+"

        while queue:
            steps += 1

            for _ in range(len(queue)):
                node = queue.popleft()

                for neighbor in get_neighbors(node):
                    r, c = neighbor
                    if maze[r][c] == ".":
                        if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                            return steps

                        queue.append(neighbor)
                        maze[r][c] = "+"

        return -1


# @lc code=end
