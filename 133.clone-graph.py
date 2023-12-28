#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# @lc code=start
from typing import Optional
from collections import defaultdict
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def clone(node: Optional['Node']) -> Optional['Node']:
            if not node:
                return None
            
            if node in visited:
                return visited[node]
            
            cloned = Node(node.val)
            visited[node] = cloned
            
            for neighbor in node.neighbors:
                cloned.neighbors.append(clone(neighbor))
            
            return cloned
        
        visited = defaultdict()
        
        return clone(node)
# @lc code=end

