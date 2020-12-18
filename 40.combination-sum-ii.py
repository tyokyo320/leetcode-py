#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []

        # 用sort对candidates进行排序，遇到比target大的数字直接break
        candidates.sort()
        self.candidates = candidates

        self.dfs(0, [], target)

        return self.res
    
    def dfs(self, start, path, target):
        if target == 0:
            self.res.append(path)
            return

        for i in range(start, len(self.candidates)):
            # eg.[10] > target(8) 一定不满足
            if self.candidates[i] > target:
                break

            if i > start and self.candidates[i] == self.candidates[i-1]:
                continue

            self.dfs(i+1, path+[self.candidates[i]], target-self.candidates[i])


# @lc code=end

