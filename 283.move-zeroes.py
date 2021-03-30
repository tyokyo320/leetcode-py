#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        方法1：

        result = []
        for i in nums:
            if i != 0:
                result.append(i)
        
        diff = len(nums) - len(result)
        while diff:
            result.append(0)
            diff -= 1
        
        nums[:] = result[:]
        '''

        '''
        方法2：

        n = nums.count(0)
        for i in range(n):
            nums.remove(0)
            nums.append(0)
        '''

        '''
        方法3：two-pointer

        '''

        l = r = 0
        while r < len(nums):
            if nums[r] == 0:
                r += 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1

# @lc code=end

