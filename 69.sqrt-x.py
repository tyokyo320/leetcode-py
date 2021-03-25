#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
import math


class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        方法1：

        return int(x ** 0.5)
        '''

        '''
        方法2：math模块
        '''

        return math.floor(math.sqrt(x))
# @lc code=end
