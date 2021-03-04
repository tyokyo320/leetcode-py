#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        # 方法1：set
        if len(set(nums)) < len(nums):
            return True
        else:
            return False
        '''

        # 方法2：hash
        hashmap = {}
        for i in nums:
            if i in hashmap:
                return True
            else:
                # 不在hash里面就让这个key设置为1
                hashmap[i] = 1
                # {1: 1}
                # {1: 1, 2: 1}
                # {1: 1, 2: 1, 3: 1}
        return False


            
            
# @lc code=end

