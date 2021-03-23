#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        '''
        方法1：split()
        '''
        # 纯空格
        if s.isspace():
            return len(s.strip())
        
        return len(s.split()[-1])

# @lc code=end

