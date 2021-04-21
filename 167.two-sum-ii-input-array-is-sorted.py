#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        方法1：two-pointer
        '''

        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return (left + 1, right + 1)
            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
# @lc code=end

