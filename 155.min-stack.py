#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.min = []


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if not self.min:
            self.min.append(x)
        else:
            if x < self.min[-1]:
                self.min.append(x)
            else:
                self.min.append(self.min[-1])

        self.stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.stack == []:
            return False
        else:
            self.min.pop()
            return self.stack.pop()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.stack == []:
            return False
        else:
            return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        # temp = self.stack[0]
        # for i in self.stack:
        #     if i < temp:
        #         temp = i
        # return temp
                
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

