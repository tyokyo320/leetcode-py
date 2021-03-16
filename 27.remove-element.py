#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        方法1：
        while val in nums:
            nums.remove(val)
        return len(nums)
        '''

        '''
        方法2：filter
        nums[:] = filter(lambda x: x != val, nums)
        return len(nums)
        '''

        '''
        方法3：two-pointer
        '''
        low, high = 0, len(nums) - 1

        while 1:
            while low < len(nums) and nums[low] != val:
                low += 1

            while high >= 0 and nums[high] == val:
                high -= 1

            if low >= high:
                break

            nums[low], nums[high] = nums[high], nums[low]
        return low


# @lc code=end
