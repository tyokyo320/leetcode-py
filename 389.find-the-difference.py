#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0:
            return t

        sum_s, sum_t = 0, 0
        for i in s:
            sum_s += ord(i)
        for j in t:
            sum_t += ord(j)

        return chr(sum_t - sum_s)
# @lc code=end
