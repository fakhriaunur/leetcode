#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def push(self, x: int) -> None:
        self.stk1.append(x)

    def pop(self) -> int:
        self.move()
        return self.stk2.pop()
        

    def peek(self) -> int:
        self.move()
        return self.stk2[-1]
        

    def empty(self) -> bool:
        return not self.stk1 and not self.stk2
    
    def move(self) -> None:
        if not self.stk2:
            while self.stk1:
                self.stk2.append(self.stk1.pop())
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

