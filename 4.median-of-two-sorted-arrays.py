#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
import numpy as np


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        方法1：numpy

        '''
        merge_list = nums1 + nums2
        return np.median(merge_list)

# @lc code=end
