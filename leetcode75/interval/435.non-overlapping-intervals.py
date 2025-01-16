#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

from typing import List


# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort based on the end times
        intervals.sort(key=lambda x: x[1])

        count = 0
        first_end = intervals[0][1]
        # for i in range(1, len(intervals)):
        #     curr_start, curr_end = intervals[i]
        for curr_start, curr_end in intervals[1:]:
            if first_end > curr_start:
                count += 1

            else:
                first_end = curr_end

        return count


# @lc code=end
