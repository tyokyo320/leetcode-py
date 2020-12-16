#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        result = ""
        stack = []
        for i in range(len(num)):
            number = int(num[i])
            # 当栈不空，栈顶元素大于数number，仍可以删
            while len(stack) != 0 and (stack[-1] > number) and k > 0:
                # 弹出栈顶元素
                stack.pop()
                k -= 1
            
            # 循环结束时候应该往栈里添加元素，number不是0直接添加。是0的话要看栈是不是空的
            if number != 0 or len(stack) != 0:
                stack.append(number)
        
        # 如果栈不空，仍然可以删除数字
        while len(stack) != 0 and k > 0:
            stack.pop()
            k -= 1
        
        stack_str = [str(i) for i in stack]
        result = "".join(stack_str)

        if result == "":
            result = "0"
        
        return result


# @lc code=end

