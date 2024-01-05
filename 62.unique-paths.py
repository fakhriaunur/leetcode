#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path_counts = [1] * n
        
        for _ in range(1, m):
            for col in range(1, n):
                path_counts[col] += path_counts[col-1]
        
        return path_counts[-1]
# @lc code=end

