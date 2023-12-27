#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        dist_mat = [[-1] * cols for _ in range(rows)]
        queue = []
        
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    dist_mat[row][col] = 0
                    queue.append((row, col))
        
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
        
        while queue:
            row, col = queue.pop(0)
            for delta_row, delta_col in directions:
                neighbor_row = row + delta_row
                neighbor_col = col + delta_col
                
                if (
                    0 <= neighbor_row < rows and
                    0 <= neighbor_col < cols and
                    dist_mat[neighbor_row][neighbor_col] == -1
                ):
                    dist_mat[neighbor_row][neighbor_col] = dist_mat[row][col] + 1
                    queue.append((neighbor_row, neighbor_col))
        
        return dist_mat
        
# @lc code=end

