#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"

        window_count = 0
        for i in range(k):
            window_count += 1 if s[i] in vowels else 0

        max_count = window_count

        for right in range(k, len(s)):
            left = right - k
            window_count -= 1 if s[left] in vowels else 0
            window_count += 1 if s[right] in vowels else 0
            max_count = max(max_count, window_count)

        return max_count


# @lc code=end
