#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

from typing import List
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(i: int, path: List[int], used: List[bool], res: List[List[int]]) -> None:
            if i == len(nums):
                res.append(path.copy())
            
            for j, num in enumerate(nums):
                if used[j]:
                    continue
                
                path.append(num)
                used[j] = True
                
                dfs(i+1, path, used, res)
                
                path.pop()
                used[j] = False
        
        curr_perms = []
        vis = [False] * len(nums)
        perms = []
        
        dfs(0, curr_perms, vis, perms)
        
        return perms
# @lc code=end

