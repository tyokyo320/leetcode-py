#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start

# import math

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        '''
        方法1：math
        return math.sqrt(num) == int(math.sqrt(num))
        '''

        '''
        方法2：binary-search
        '''
        left, right = 0, num
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                right = mid - 1
            else:
                left = mid + 1
        return False

# @lc code=end
