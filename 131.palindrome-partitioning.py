#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

from typing import List


# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromes = []

        def dfs(start_index: int, path: List[str]):
            if start_index == len(s):
                palindromes.append(path[:])
                return

            n = len(s)
            for end_index in range(start_index + 1, n + 1):
                prefix = s[start_index:end_index]

                if prefix == prefix[::-1]:
                    dfs(end_index, path + [prefix])

        dfs(0, [])

        return palindromes


# @lc code=end
