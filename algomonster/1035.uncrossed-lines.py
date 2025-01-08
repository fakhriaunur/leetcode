#
# @lc app=leetcode id=1035 lang=python3
#
# [1035] Uncrossed Lines
#

from typing import List


# @lc code=start
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(1, m + 1):
            for c in range(1, n + 1):
                if nums1[r - 1] == nums2[c - 1]:
                    prev_diag = dp[r - 1][c - 1]
                    dp[r][c] = prev_diag + 1
                else:
                    prev_top = dp[r - 1][c]
                    prev_left = dp[r][c - 1]
                    dp[r][c] = max(prev_top, prev_left)

        # print(dp)
        return dp[m][n]


# @lc code=end
