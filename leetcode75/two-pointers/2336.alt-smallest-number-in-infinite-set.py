#
# @lc app=leetcode id=2336 lang=python3
#
# [2336] Smallest Number in Infinite Set
#


# @lc code=start
class SmallestInfiniteSet:
    def __init__(self):
        self.infinite_set = set()

    def popSmallest(self) -> int:
        i = 1

        while i in self.infinite_set:
            i += 1

        self.infinite_set.add(i)

        return i

    def addBack(self, num: int) -> None:
        self.infinite_set.discard(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# @lc code=end
