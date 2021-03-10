#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        方法1：sort
        '''
        nums1.sort()

        result = []
        for i in nums1:
            if i in nums2 and i not in result:
                result.append(i)
        
        return result

# @lc code=end

