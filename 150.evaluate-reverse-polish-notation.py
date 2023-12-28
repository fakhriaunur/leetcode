#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

from typing import List
# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        
        for token in tokens:
            if token.isdigit() or len(token) > 1:
                nums.append(int(token))
            else:
                if token == '+':
                    nums[-2] += nums[-1]
                elif token == '-':
                    nums[-2] -= nums[-1]
                elif token == '*':
                    nums[-2] *= nums[-1]
                else:
                    nums[-2] = int(float(nums[-2] / nums[-1]))
                nums.pop()
        
        return nums[0]
# @lc code=end

