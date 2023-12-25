#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        pointer_a = len(a) - 1
        pointer_b = len(b) - 1
        carry = 0
        
        while (
            pointer_a >= 0
            or pointer_b >= 0
            or carry
        ):
            carry += (
                (0 if pointer_a < 0 else int(a[pointer_a]))
                + (0 if pointer_b < 0 else int(b[pointer_b]))
            )
            carry, bit_value = divmod(carry, 2)
            result.append(str(bit_value))
            pointer_a -= 1
            pointer_b -= 1
        
        return "".join(result[::-1])
# @lc code=end

