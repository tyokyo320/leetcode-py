#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        result = []

        for i in range(len(nums) - 1):
            for j in range(1, len(nums)):
                if i != j and nums[i] + nums[j] ==  target:
                    if i not in result:
                        result.append(i)
                    if j not in result:
                        result.append(j)
                if len(result) == 2:
                    break
            if len(result) == 2:
                break
        return result
        '''

        '''
        方法2：hash
        '''
        hashmap = {}
        for i, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target - num], i]
            hashmap[num] = i
                
# @lc code=end

