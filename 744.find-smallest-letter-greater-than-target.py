#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        '''
        方法1：

        for letter in letters:
            if letter > target:
                return letter
        return letters[0]
        '''

        '''
        方法2：Binary Search
        '''
        l, r = 0, len(letters) - 1
        while l < r:
            mid = (l + r) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return letters[l] if letters[l] > target else letters[0]


# @lc code=end
