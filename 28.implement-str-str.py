#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        方法1：index()返回值：如果包含子字符串返回开始的索引值，否则抛出异常
        if needle in haystack:
            return haystack.index(needle)
        return -1
        '''

        '''
        方法2：find()返回值：如果包含子字符串返回开始的索引值，否则返回-1
        return haystack.find(needle)
        '''

        '''
        方法3：two-pointer
        '''
        n = len(needle)
        h = len(haystack)
        if n < 1 or needle == haystack:
            return 0
        if h < 1:
            return -1

        for i, c in enumerate(haystack):
            # n > h - i 这个需要加上，假设haystack为1001位，needle有1000位，移动2次后没找到可以直接不用计算了（999<1000）
            if n > h - i:
                return -1
            if c == needle[0] and all([haystack[i+j] == needle[j] for j in range(1, n)]):
                return i

        return -1


# @lc code=end
