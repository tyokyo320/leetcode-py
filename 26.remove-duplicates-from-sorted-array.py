#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        方法1：
        slow = 0

        while slow + 1 < len(nums):
            if nums[slow] == nums[slow + 1]:
                nums.remove(nums[slow])
            else:
                slow += 1
        
        return len(nums)
        '''

        '''
        方法2：
        '''
        # Without "[:]", you're creating a new list object
        nums[:] = sorted(set(nums))
        return len(nums)

# @lc code=end

