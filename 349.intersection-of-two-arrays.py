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
        nums1.sort()

        result = []
        for i in nums1:
            if i in nums2 and i not in result:
                result.append(i)

        return result
        '''

        '''
        方法2：set
        return set(nums1) & set(nums2)
        '''

        '''
        方法3：two-pointer
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
                if nums1[i] not in result:
                    result.append(nums1[i])
                i += 1
                j += 1
        return result
        '''

        '''
        方法4：hash
        hashmap = {}
        result = []
        for n in nums1:
            hashmap[n] = 1

        for n in nums2:
            # Check if n is in dictionary and not in the result
            if n in hashmap and hashmap[n]:
                result.append(n)
                # It will set the value of hashmap[n] = 0 which will indicate we already added n in result
                hashmap[n] -= 1
        return result
        '''

        '''
        方法5：binary-search
        '''
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        
        result = []
        nums1 = sorted(nums1)
        nums2 = set(nums2)

        for i in nums2:
            left, right = 0, len(nums1) - 1
            while left <= right:
                mid = (right + left) >> 1
                if nums1[mid] == i:
                    result.append(nums1[mid])
                    break
                else:
                    if nums1[mid] < i:
                        left = mid + 1
                    else:
                        right = mid - 1
        return result
# @lc code=end
