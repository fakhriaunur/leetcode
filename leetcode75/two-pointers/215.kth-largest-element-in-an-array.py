#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# from heapq import _heapify_max as heapify, heappop

from heapq import heapify, heappop
from typing import List


# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # max heap
        nums = [-x for x in nums]
        heapify(nums)
        # print(nums)

        for _ in range(k - 1):
            heappop(nums)

        # print(nums)
        return -nums[0]


# @lc code=end
