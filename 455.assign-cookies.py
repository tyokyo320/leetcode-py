#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        s.sort()
        g.sort()

        for cookies in s:
            if g:
                if g[0] <= cookies:
                    g.pop(0)
                    count += 1
            else:
                break

        return count
# @lc code=end

