#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        方法1：

        if target not in nums:
            nums.append(target)
            nums.sort()
        return nums.index(target)
        '''

        '''
        方法2：Binary Search
        '''
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
        return low
# @lc code=end

