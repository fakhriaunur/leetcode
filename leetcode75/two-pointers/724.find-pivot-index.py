#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

from typing import List


# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)

        for i in range(len(nums)):
            right_sum -= nums[i]

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1

        # left_sum = []
        # right_sum = []
        # for i in range(len(nums)):
        #     # left_sum[i] = sum(nums[:i])
        #     # left_sum = [0]
        #     # left_sum.append(left_sum[-1] + sum(nums[:i]))
        #     left_sum.append(sum(nums[:i]))

        #     # right_sum[i] = sum(nums[i:])
        #     # right_sum = [0]
        #     right_sum.append(sum(nums[i:]))

        #     if left_sum[i] == right_sum[i]:
        #         return i

        # return -1


# @lc code=end
