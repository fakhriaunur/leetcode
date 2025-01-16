#
# @lc app=leetcode id=901 lang=python3
#
# [901] Online Stock Span
#

# @lc code=start
class StockSpanner:
    def __init__(self):
        # list of price, index tuple
        self.stack: list[tuple[int, int]] = []

    def next(self, price: int) -> int:
        span_count = 1

        while self.stack and price >= self.stack[-1][0]:
            span_count += self.stack.pop()[1]

        self.stack.append((price, span_count))

        return span_count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end
