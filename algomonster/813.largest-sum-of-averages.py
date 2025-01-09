#
# @lc app=leetcode id=813 lang=python3
#
# [813] Largest Sum of Averages
#

from itertools import accumulate
from typing import List


# @lc code=start
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        prefix_sums = list(accumulate(nums, initial=0))

        def subarray_sum(i: int, j: int) -> int:
            return prefix_sums[j] - prefix_sums[i]

        n = len(nums)

        dp = [[0.0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][1] = subarray_sum(0, i) / i

        for i in range(1, n + 1):
            for j in range(2, k + 1):
                for p in range(j - 1, i):
                    best_split = dp[p][j - 1] + subarray_sum(p, i) / (i - p)
                    dp[i][j] = max(dp[i][j], best_split)

        # for r in dp:
        #     print(r)
        return dp[n][k]


# @lc code=end
