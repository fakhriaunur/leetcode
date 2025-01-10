#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

from typing import List


# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target

        for i in range(1, target + 1):
            for x in nums:
                if i >= x:
                    dp[i] += dp[i - x]

        print(dp)
        return dp[target]


# @lc code=end
