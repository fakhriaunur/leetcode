#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
from typing import List
# @lc code=start
from itertools import pairwise
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row: int, col: int) -> None:
            grid[row][col] = '0'
            
            for delta_row, delta_col in pairwise(dirs):
                neighbor_row = row + delta_row
                neighbor_col = col + delta_col
                
                if (
                    0 <= neighbor_row < rows
                    and 0 <= neighbor_col < cols
                    and grid[neighbor_row][neighbor_col] == '1'
                ):
                    dfs(neighbor_row, neighbor_col)
        
        islands_count = 0
        dirs = (-1, 0, 1, 0, -1)
        rows, cols = len(grid), len(grid[0])
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    dfs(row, col)
                    islands_count += 1
        
        return islands_count
# @lc code=end

