#
# @lc app=leetcode id=576 lang=python3
#
# [576] Out of Boundary Paths
#

# @lc code=start
from functools import lru_cache


class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        @lru_cache(maxsize=None)
        def dfs(rem_moves, row, col):
            if not (0 <= row < m and 0 <= col < n):
                return 1

            if rem_moves <= 0:
                return 0

            path_counts = 0

            dirs = [
                (-1, 0),
                (0, -1),
                (1, 0),
                (0, 1),
            ]

            for d_row, d_col in dirs:
                n_row = row + d_row
                n_col = col + d_col

                path_counts += dfs(rem_moves - 1, n_row, n_col)

                path_counts %= MOD

            return path_counts

        MOD = 10**9 + 7

        return dfs(maxMove, startRow, startColumn)


# @lc code=end
