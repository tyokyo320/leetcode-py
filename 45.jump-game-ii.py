#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        # 如果数组长度小于2，则说明不用跳跃，返回0
        if len(nums) < 2:
            return 0
        
        # 当前可达到的最远位置
        current_max_index = nums[0]
        # 遍历各个位置过程中，可达到的最远位置
        pre_max_max_index = nums[0]

        jump_min = 1

        for i in range(1, len(nums)):
            # 若无法再想起移动了，才进行跳跃
            if i > current_max_index:
                jump_min += 1
                # 更新当前可达到的最远位置
                current_max_index = pre_max_max_index
            
            if pre_max_max_index < nums[i] + i:
                # 更新pre_max_max_index
                pre_max_max_index = nums[i] + i
            
        return jump_min

# @lc code=end
