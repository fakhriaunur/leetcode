#
# @lc app=leetcode id=2462 lang=python3
#
# [2462] Total Cost to Hire K Workers
#

from heapq import heapify, heappop, heappush
from typing import List


# @lc code=start
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        min_heap = []
        n = len(costs)

        left = candidates - 1
        right = n - candidates

        for i in range(candidates):
            min_heap.append((costs[i], i))

        for i in range(n - candidates, n):
            if i > left:
                min_heap.append((costs[i], i))

        heapify(min_heap)

        total_cost = 0

        for _ in range(k):
            cost, i = heappop(min_heap)
            total_cost += cost

            if i <= left:
                left += 1
                if left < right:
                    heappush(min_heap, (costs[left], left))

            if i >= right:
                right -= 1
                if left < right:
                    heappush(min_heap, (costs[right], right))

        return total_cost


# @lc code=end
