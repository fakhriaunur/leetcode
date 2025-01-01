#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

from typing import List


# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # subarray_sum = 0.0
        # for i in range(k):
        #     subarray_sum += nums[i]
        subarray_sum = sum(nums[:k])

        max_sum = subarray_sum

        for right in range(k, len(nums)):
            left = right - k

            # subarray_sum -= nums[left]
            # subarray_sum += nums[right]
            subarray_sum += nums[right] - nums[left]

            max_sum = max(max_sum, subarray_sum)

        return max_sum / k


# @lc code=end
