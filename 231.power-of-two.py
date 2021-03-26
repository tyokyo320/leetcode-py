#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
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
        return n > 0 and not (n & n-1)
        '''

        '''
        方法3的写法2：

        If n is the power of two:

        n = 2 ^ 0 = 1 = 0b0000...00000001, and (n - 1) = 0 = 0b0000...0000.
        n = 2 ^ 1 = 2 = 0b0000...00000010, and (n - 1) = 1 = 0b0000...0001.
        n = 2 ^ 2 = 4 = 0b0000...00000100, and (n - 1) = 3 = 0b0000...0011.
        n = 2 ^ 3 = 8 = 0b0000...00001000, and (n - 1) = 7 = 0b0000...0111.

        we have n & (n-1) == 0b0000...0000 == 0

        Otherwise, n & (n-1) != 0.
        return n > 0 and (n & n-1) == 0
        '''

        '''
        方法4：math库log
        '''
        from math import log
        if n <= 0 :
            return False
        A = round(log(n,2))
        return 2**A == n

# @lc code=end
