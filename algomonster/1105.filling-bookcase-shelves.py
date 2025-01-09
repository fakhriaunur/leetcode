#
# @lc app=leetcode id=1105 lang=python3
#
# [1105] Filling Bookcase Shelves
#

from typing import List


# @lc code=start
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            width, height = books[i - 1]
            dp[i] = dp[i - 1] + height
            total_width = width

            for j in range(i - 1, 0, -1):
                total_width += books[j - 1][0]

                if total_width > shelfWidth:
                    break

                height = max(height, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + height)

        # print(dp)
        return dp[n]


# @lc code=end
