#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

from typing import List


# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        for diff in gain:
            altitudes.append(altitudes[-1] + diff)

        return max(altitudes)


# @lc code=end
