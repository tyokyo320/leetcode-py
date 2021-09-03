#
# @lc app=leetcode id=1186 lang=python3
#
# [1186] Maximum Subarray Sum with One Deletion
#

# @lc code=start
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        
        delete, keep = float('-inf'), float('-inf')
        ans = float('-inf')

        for num in arr:
            keep, delete = max(keep+num, num), max(keep, delete+num)
            print(keep, delete)
            ans = max(keep, delete, ans)

        return ans

# @lc code=end

