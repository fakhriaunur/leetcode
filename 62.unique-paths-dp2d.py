#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path_counts = [[1] * n for _ in range(m)]
        
        for row in range(1, m):
            for col in range(1, n):
                path_counts[row][col] = path_counts[row][col-1] + path_counts[row-1][col]
        
        return path_counts[-1][-1]
# @lc code=end

