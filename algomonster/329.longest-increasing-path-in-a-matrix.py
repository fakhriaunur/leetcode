#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#

from functools import lru_cache

# from itertools import pairwise
from typing import List


# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        # why is it not working?
        # dirs = pairwise([-1, 0, 1, 0, -1])
        dirs = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1),
        ]

        @lru_cache(maxsize=None)
        def dfs(row: int, col: int) -> int:
            max_path_length = 1

            for d_row, d_col in dirs:
                n_row = row + d_row
                n_col = col + d_col

                if (
                    0 <= n_row < rows
                    and 0 <= n_col < cols
                    and matrix[n_row][n_col] > matrix[row][col]
                ):
                    max_path_length = max(max_path_length, dfs(n_row, n_col) + 1)

            return max_path_length

        max_path = 0
        for r in range(rows):
            for c in range(cols):
                max_path = max(max_path, dfs(r, c))
                # print(max_path)

        dfs.cache_clear()

        return max_path


# @lc code=end
