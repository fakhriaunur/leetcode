#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i: int, path: List[int], res: List[List[int]]) -> None:
            if i == len(nums):
                res.append(path.copy())
                return
            
            dfs(i+1, path, res)
            path.append(nums[i])
            dfs(i+1, path, res)
            path.pop()
        
        all_subsets = []
        curr_subset = []
        
        dfs(0, curr_subset, all_subsets)
        
        return all_subsets
# @lc code=end

