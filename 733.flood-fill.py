#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
from typing import List
from itertools import pairwise
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def fill_helper(row: int, col: int):
            if (
                not 0 <= row < height
                or not 0 <= col < width
                or image[row][col] != original_color
                or image[row][col] == color
            ):
                return
            
            image[row][col] = color
            
            for delta_row, delta_col in pairwise(direction):
                fill_helper(row + delta_row, col + delta_col)
        
        direction = [-1, 0, 1, 0, -1]
        height, width = len(image), len(image[0])
        original_color = image[sr][sc]
        fill_helper(sr, sc)
        
        return image
# @lc code=end

