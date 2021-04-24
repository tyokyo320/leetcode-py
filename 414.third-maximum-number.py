#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        '''
        方法1：暴力法

        temp = []
        temp[:] = nums[:]
        if len(nums) < 3:
            return max(nums)
        
        nums.sort(reverse=True)
        # 去除第一大的数字
        first = nums[0]
        for i in range(len(nums)):
            if first in nums:
                nums.remove(first)
        # 去除第二大数字
        # case: [1, 1, 2]
        if len(nums) == 0:
            return max(temp)
        else:
            second = nums[0]
            for i in range(len(nums)):
                if second in nums:
                    nums.remove(second)
        # case: [1, 1, 1]
        if len(nums) == 0:
            return max(temp)
        return nums[0]
        '''

        '''
        方法2：set去重
        '''
        nums = sorted(list(set(nums)), reverse=True)
        return nums[0] if len(nums) < 3 else nums[2]
# @lc code=end

