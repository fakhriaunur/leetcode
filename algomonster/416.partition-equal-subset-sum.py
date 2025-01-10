#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

from typing import List


# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)

        if s % 2 == 1:
            return False

        dp = [[False] * (s // 2 + 1) for _ in range(n + 1)]

        dp[0][0] = True

        for r in range(1, n + 1):
            for c in range(s // 2 + 1):
                if dp[r - 1][c]:
                    dp[r][c] = True

                if c >= nums[r - 1] and dp[r - 1][c - nums[r - 1]]:
                    dp[r][c] = True

        return dp[n][s // 2]


# @lc code=end
