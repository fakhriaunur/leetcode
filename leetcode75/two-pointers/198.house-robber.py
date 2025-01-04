#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

from typing import List


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_exclude = 0
        prev_include = 0

        for house_value in nums:
            prev_exclude, prev_include = (
                max(prev_exclude, prev_include),
                prev_exclude + house_value,
            )

        return max(prev_exclude, prev_include)

        # dp = [0] * len(nums)
        # dp[0] = nums[0]

        # max_score = 0

        # for i in range(1, len(nums)):
        #     include = dp[i - 1] + nums[i]
        #     exclude = max(include, nums[i])
        #     max_score = max(exclude, include)
        #     dp[i] = include

        # return max_score


# @lc code=end
