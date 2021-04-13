#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start


class Solution:
    def trailingZeroes(self, n: int) -> int:
        '''
        方法1：求阶乘后的0，直接递归求阶乘数会导致溢出，所以应换思路
        最末尾出现一个0，表示有一组2*5，所以应看看质因数中有几个5
        '''
        result = 0
        while n > 0:
            n //= 5
            result += n
        return result
# @lc code=end
