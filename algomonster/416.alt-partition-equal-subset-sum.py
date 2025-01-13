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

        dp = [[False] * (s // 2 + 1) for _ in range(2)]

        dp[0][0] = True

        for r in range(1, n + 1):
            for c in range(s // 2 + 1):
                if dp[0][c]:
                    dp[1][c] = True

                if c >= nums[r - 1] and dp[0][c - nums[r - 1]]:
                    dp[1][c] = True

            # swap prev, curr rows
            for c in range(s // 2 + 1):
                dp[0][c] = dp[1][c]
                dp[1][c] = False

        return dp[0][s // 2]


# @lc code=end
