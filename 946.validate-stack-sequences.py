#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#

# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # 将pushed里面的数字依次入栈（stack），当stack最上面的数字与poped第一个数字相同，同时删除stack与poped相同的数字
        stack = []
        for i in range(len(pushed)):
            stack.append(pushed[i])
            # 栈最上面的是-1，而队列第一个数字是0（列表的索引-1是整个列表的最后一个！）
            while stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        # 当stack为空的时候，即合法
        return len(stack) == 0

# @lc code=end

