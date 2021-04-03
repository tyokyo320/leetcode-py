#
# @lc app=leetcode id=1399 lang=python3
#
# [1399] Count Largest Group
#

# @lc code=start
class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = {}
        for i in range(1, n + 1):
            s = sum([int(j) for j in str(i)])
            if s in d:
                d[s].append(i)
            else:
                d[s] = [i]
        
        temp = [len(i) for i in d.values()]
        return temp.count(max(temp))
# @lc code=end

