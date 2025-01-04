#
# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#

from functools import lru_cache


# @lc code=start
class Solution:
    def numTilings(self, n: int) -> int:
        @lru_cache(None)
        def count_ways(first_row: int, second_row: int) -> int:
            if first_row > n and second_row > n:
                return 0

            if first_row == n and second_row == n:
                return 1

            ways = 0

            if first_row == second_row:
                ways = (
                    count_ways(first_row + 2, second_row + 2)
                    + count_ways(first_row + 1, second_row + 1)
                    + count_ways(first_row + 2, second_row + 1)
                    + count_ways(first_row + 1, second_row + 2)
                )

            elif first_row > second_row:
                ways = count_ways(first_row, second_row + 2) + count_ways(
                    first_row + 1, second_row + 2
                )

            else:
                ways = count_ways(first_row + 2, second_row) + count_ways(
                    first_row + 2, second_row + 1
                )

            return ways % MOD

        MOD = 10**9 + 7
        return count_ways(0, 0)


# @lc code=end
