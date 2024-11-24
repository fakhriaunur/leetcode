#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def collect_leaves(root: Optional[TreeNode]) -> List[int]:
            if not root:
                return []
                
            leaves_left = collect_leaves(root.left)
            leaves_right = collect_leaves(root.right)
            
            leaves =  leaves_left + leaves_right
            
            if not leaves:
                return [root.val]
                # leaves.append(root.val)
            
            
            return leaves
            
            # return ans or [root.val]
            
        
        return collect_leaves(root1) == collect_leaves(root2)
        
        # def get_leaves(root: Optional[TreeNode], leaves: List[int]):
        #     if not root:
        #         return None
            
            
        #     if not (root.left and root.right):
        #         leaves.append(root.val)
            
        #     get_leaves(root.left, leaves)
        #     get_leaves(root.right, leaves)
            
        # leaves1 = []
        # get_leaves(root1, leaves1)
        
        # leaves2 =  []
        # get_leaves(root1, leaves2)
        
        # print(leaves1, leaves2)
        # return leaves1 == leaves2
# @lc code=end

