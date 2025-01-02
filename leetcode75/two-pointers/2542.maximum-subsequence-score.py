#
# @lc app=leetcode id=2542 lang=python3
#
# [2542] Maximum Subsequence Score
#

from heapq import heappop, heappush
from typing import List


# @lc code=start
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        num_pair = sorted(zip(nums2, nums1), reverse=True)

        min_heap = []
        sum = 0
        ans = 0

        for num2, num1 in num_pair:
            sum += num1
            heappush(min_heap, num1)

            if len(min_heap) == k:
                ans = max(ans, sum * num2)
                sum -= heappop(min_heap)

        return ans


# @lc code=end
