#
# @lc app=leetcode id=1130 lang=python3
#
# [1130] Minimum Cost Tree From Leaf Values
#

from typing import List


# @lc code=start
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        max_matrix = [[0] * n for _ in range(n)]

        for start in range(n - 1, -1, -1):
            max_matrix[start][start] = arr[start]
            for end in range(start + 1, n):
                max_matrix[start][end] = max(
                    max_matrix[start][end - 1],
                    arr[end],
                )

                dp[start][end] = float("inf")

                for k in range(start, end):
                    dp[start][end] = min(
                        dp[start][end],
                        dp[start][k]
                        + dp[k + 1][end]
                        + max_matrix[start][k] * max_matrix[k + 1][end],
                    )

        return dp[0][-1]


# @lc code=end
