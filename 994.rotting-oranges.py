#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

from typing import List
# @lc code=start
from itertools import pairwise
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time_count = 0
        fresh_count = 0
        queue = deque()
        rows, cols = len(grid), len(grid[0])
        dirs = (-1, 0, 1, 0, -1)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1
        
        while queue and fresh_count > 0:
            time_count += 1
            
            for _ in range(len(queue)):
                row, col = queue.popleft()
                
                for d_row, d_col in pairwise(dirs):
                    n_row = row + d_row
                    n_col = col + d_col
                    
                    if (
                        0 <= n_row < rows
                        and 0 <= n_col < cols
                        and grid[n_row][n_col] == 1
                    ):
                        grid[n_row][n_col] = 2
                        queue.append((n_row, n_col))
                        fresh_count -= 1
        
        return time_count if fresh_count == 0 else -1
# @lc code=end

