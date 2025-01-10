#
# @lc app=leetcode id=630 lang=python3
#
# [630] Course Schedule III
#

from heapq import heappop, heappush
from typing import List


# @lc code=start
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # sort based on the end day
        courses.sort(key=lambda x: x[1])

        max_heap = []

        total_duration = 0

        for duration, last_day in courses:
            heappush(max_heap, -duration)
            total_duration += duration

            while total_duration > last_day:
                total_duration -= -heappop(max_heap)

        # print(max_heap)
        return len(max_heap)


# @lc code=end
