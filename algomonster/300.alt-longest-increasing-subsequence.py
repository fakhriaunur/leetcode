#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

from typing import List


# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def upper_bound(dp, target):
            n = len(dp)
            lo = 0
            hi = n

            while lo < hi:
                mid = (lo + hi) >> 1
                if dp[mid] > target:
                    hi = mid
                else:
                    lo = mid + 1

            return lo

        n = len(nums)
        dp = [float("inf")] * (n + 1)

        dp[0] = -float("inf")

        for i in range(n):
            j = upper_bound(dp, nums[i])
            if dp[j - 1] < nums[i] < dp[j]:
                dp[j] = nums[i]

        ans = 0

        for i in range(n + 1):
            if dp[i] < float("inf"):
                ans = i

        return ans


# @lc code=end
