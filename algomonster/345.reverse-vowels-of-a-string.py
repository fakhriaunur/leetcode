#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        left, right = 0, len(s) - 1
        res = list(s)

        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else:
                res[left], res[right] = res[right], res[left]
                left += 1
                right -= 1

        return "".join(res)


# @lc code=end
