#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.stack == []:
            return False
        else:
            return self.stack.pop()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.stack == []:
            return False
        else:
            return self.stack[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.stack == []:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

