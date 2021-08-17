#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) == 1:
            return intervals

        result = []
        intervals = sorted(intervals)

        for i, j in enumerate(intervals):
            if i == 0:
                result.append([j[0], j[1]])
            else:
                # 现在列表第一个元素要比前一个列表的第二个元素小时
                if j[0] <= result[-1][-1] and j[1] > result[-1][-1]:
                    result[-1][-1] = j[1]
                # [[1, 4], [2, 3]]时，保持原状
                elif j[0] <= result[-1][-1] and j[1] <= result[-1][-1]:
                    pass
                else:
                    result.append([j[0], j[1]])
        return result
# @lc code=end
