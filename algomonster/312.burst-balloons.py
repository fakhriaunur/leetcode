#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

from typing import List


# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # TODO: benefits of padding with ones?
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for start in range(n - length):
                end = start + length

                for k in range(start + 1, end):
                    dp[start][end] = max(
                        dp[start][end],
                        dp[start][k] + dp[k][end] + nums[start] * nums[k] * nums[end],
                    )

        # for r in dp:
        #     print(r)
        return dp[0][-1]


# @lc code=end
