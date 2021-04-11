#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = dict()
        hashmap_t = dict()


        for i in s:
            if i not in hashmap_s:
                hashmap_s[i] = 1
            else:
                hashmap_s[i] += 1
        
        for j in t:
            if j not in hashmap_t:
                hashmap_t[j] = 1
            else:
                hashmap_t[j] += 1
        
        return hashmap_s == hashmap_t
# @lc code=end

