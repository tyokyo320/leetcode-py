#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        方法1：counting sort思想

        bucket = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            bucket[nums[i]] += 1
        
        for i, j in enumerate(bucket):
            if j == 0:
                return i
        '''

        '''
        方法2：

        '''
        return sum(range(len(nums) + 1)) - sum(nums)

# @lc code=end

