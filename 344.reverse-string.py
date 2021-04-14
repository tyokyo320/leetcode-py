#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        '''
        方法1：
        
        print(s.reverse())
        '''

        '''
        方法2：[::-1]
        
        s[:] = s[::-1]
        '''

        '''
        方法3：two-pointer
        '''
        low, high = 0, len(s) - 1
        while low < high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1
        return s

# @lc code=end
