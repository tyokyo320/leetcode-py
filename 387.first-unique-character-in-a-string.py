#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''
        方法1：计数器

        hashmap = collections.Counter(s)
        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                return i
        return -1
        '''

        '''
        方法2：hash-table

        '''
        hashmap = dict()
        for i in s:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        
        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                return i
        return -1

# @lc code=end

