#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s: str) -> bool:
            left, right = 0, len(s) - 1

            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        #     n = len(s) - 1
        #     for i in range(n // 2 + 1):
        #         if s[i] != s[n - i]:
        #             return False

        #     return True

        # n = len(s) - 1
        # for i in range(n // 2 + 1):
        #     if s[i] != s[n - i]:
        #         return is_palindrome(s[i + 1 : n - i + 1]) or is_palindrome(
        #             s[i : n - i]
        #         )

        # return True

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return is_palindrome(s[left + 1 : right + 1]) or is_palindrome(
                    s[left:right]
                )

            left += 1
            right -= 1

        return True


# @lc code=end
