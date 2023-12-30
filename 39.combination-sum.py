#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i: int, rem: int) -> None:
            if rem == 0:
                ans.append(temp.copy())
                return
            
            if i >= len(candidates) or rem < candidates[i]:
                return
            
            dfs(i+1, rem)
            temp.append(candidates[i])
            dfs(i, rem - candidates[i])
            temp.pop()
        
        candidates.sort()
        
        temp = []
        ans = []
        dfs(0, target)
        
        return ans
# @lc code=end

