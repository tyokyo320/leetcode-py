#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        '''
        方法1：slice

        nums1[m:] = nums2[:n]
        nums1.sort()
        '''

        '''
        方法2：two-pointer

        '''
        temp = []
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1

        if i < m:
            temp += nums1[i:m]
        if j < n:
            temp += nums2[j:n]
        
        nums1.clear()
        nums1 += temp
# @lc code=end

