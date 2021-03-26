#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        '''
        方法1：
        convert to binary and count how many 1 in binary, 2 to the power must only contains one 1 and followed by 0(s)
        
        return n > 0 and bin(n).count('1') == 1
        '''

        '''
        方法2：
        Brute force -- n divided by 2 and check mod == 0 or not until n == 1

        if n <= 0:
            return False
        
        while n % 2 == 0:
            n //= 2
        return True if n == 1 else False
        '''

        '''
        方法3：
        如果两个相应位都为1,则该位的结果为1,否则为0
        bitwise comparison -- 2 to the power must be converted to binary number that only contains one 1 and followed by all 0s; while 2 to the power minus 1 must be initialized 0 and followed by all 1s , so x & (x-1) = 0
        '''
        return n > 0 and not (n & n-1)


        
# @lc code=end

