#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

from typing import List


# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)

        max_len = 0
        for i in range(1, n + 1):
            ni = nums[i - 1]
            dp[i] = dp[0] + 1

            for j in range(1, i):
                nj = nums[j - 1]
                if nj < ni:
                    dp[i] = max(dp[i], dp[j] + 1)

            max_len = max(max_len, dp[i])

        return max_len


# @lc code=end
