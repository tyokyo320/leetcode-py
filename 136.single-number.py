#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        方法1：hashmap
        '''
        hashmap = dict()

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        
        for key, value in hashmap.items():
            if value == 1:
                return key

# @lc code=end

