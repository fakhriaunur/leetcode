#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

from typing import List


# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_alt = 0
        max_alt = curr_alt

        for diff in gain:
            curr_alt += diff
            max_alt = max(max_alt, curr_alt)

        return max_alt


# @lc code=end
