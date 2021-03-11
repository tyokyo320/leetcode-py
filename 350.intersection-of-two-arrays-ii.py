#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        方法1：
        result = []

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                nums2.remove(nums1[i])
                result.append(nums1[i])

        return result
        '''

        '''
        方法2：two-pointer
        result = []
        nums1.sort()
        nums2.sort()
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1
                
        return result
        '''

        '''
        方法3：binary-search
        '''
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        result = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        for i in nums2:
            left, right = 0, len(nums1) - 1
            while left <= right:
                mid = (right + left) >> 1
                if nums1[mid] == i:
                    result.append(nums1[mid])
                    nums1.remove(nums1[mid])
                    break
                else:
                    if nums1[mid] < i:
                        left = mid + 1
                    else:
                        right = mid - 1
        return result

# @lc code=end

