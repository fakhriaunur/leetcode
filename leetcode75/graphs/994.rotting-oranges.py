#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

from collections import deque
from itertools import pairwise
from typing import List


# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])

        def get_neighbors(coord: tuple[int, int]) -> List[tuple[int, int]]:
            row, col = coord
            dirs = pairwise([-1, 0, 1, 0, -1])
            neighbors = []

            for d_row, d_col in dirs:
                n_row = row + d_row
                n_col = col + d_col

                if 0 <= n_row < num_rows and 0 <= n_col < num_cols:
                    neighbors.append((n_row, n_col))

            return neighbors

        # TODO: composite function to count fresh apples in the grid
        # fresh_only = filter(lambda col: col == 1, [col for col in grid])
        # fresh_count = sum(fresh_only)
        # freshman_count = sum(
        #     filter(lambda col: col == 1, map(lambda row: row in grid, grid))
        # )
        # print(list(row))

        queue = deque()

        count_fresh = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 1:
                    count_fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        minutes_passed = 0

        while queue and count_fresh:
            minutes_passed += 1
            for _ in range(len(queue)):
                rotten_node = queue.popleft()

                for r, c in get_neighbors(rotten_node):
                    if grid[r][c] == 1:
                        grid[r][c] = 2
                        count_fresh -= 1
                        queue.append((r, c))

        return minutes_passed if count_fresh == 0 else -1


# @lc code=end
