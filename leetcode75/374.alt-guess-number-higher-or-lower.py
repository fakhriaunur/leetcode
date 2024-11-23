#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

def guess(num: int) -> int:
    return 0
# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        
        while left < right:
            mid = left + ((right - left) >> 1)
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                left = mid + 1
            elif guess(mid) == -1:
                right = mid
            
        return left
# @lc code=end

