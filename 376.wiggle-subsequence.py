#
# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 序列个数小于2时直接为摇摆序列
        if len(nums) < 2:
            return len(nums)
        
        # 利用自动机，设置扫描时的三种状态
        BEGIN = 0
        UP = 1
        DOWN = 2

        # 初始化，摇摆序列最大长度至少为1
        STATE = BEGIN
        max_length = 1

        # 从第二个元素开始扫描
        for i in range(1, len(nums)):
            if STATE == BEGIN:
                if nums[i-1] < nums[i]:
                    STATE = UP
                    max_length += 1
                elif nums[i-1] > nums[i]:
                    STATE = DOWN
                    max_length += 1
            if STATE == UP:
                if nums[i-1] > nums[i]:
                    STATE = DOWN
                    max_length += 1
            if STATE == DOWN:
                if nums[i-1] < nums[i]:
                    STATE = UP
                    max_length += 1
        return max_length

# @lc code=end

