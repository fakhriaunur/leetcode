#
# @lc app=leetcode id=2336 lang=python3
#
# [2336] Smallest Number in Infinite Set
#

from heapq import heapify, heappush, heappop


# @lc code=start
class SmallestInfiniteSet:
    def __init__(self):
        self.infinite_set = [x for x in range(1, 1001)]
        heapify(self.infinite_set)

    def popSmallest(self) -> int:
        return heappop(self.infinite_set)

    def addBack(self, num: int) -> None:
        if num not in self.infinite_set:
            heappush(self.infinite_set, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# @lc code=end
