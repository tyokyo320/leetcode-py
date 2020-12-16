#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index = []
        for i in range(len(nums)):
            # 计算index数组（index = 位置i + 最远nums）
            index.append(i+nums[i])
        
        # jump开始扫描，初始化
        jump = 0
        max_index = index[0]

        # 不能超过数组，也不可超过当前最远到达的位置
        while jump < len(index) and jump <= max_index:
            if max_index < index[jump]:
                # 若当前可以跳更远，则更新max_index
                max_index = index[jump]
            # 扫描
            jump += 1
        
        # jump达到数组尾部，则返回真
        if jump == len(index):
            return True

        return False

# @lc code=end

