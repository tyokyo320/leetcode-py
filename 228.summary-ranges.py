#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        length = len(nums)
        if length == 0:
            return []

        # 给数组最后加一个正无穷，防止遍历的时候数组越界
        nums.append(float("inf"))

        result, start = [], 0
        for i in range(length):
            # 不相邻
            if nums[i+1] != nums[i] + 1:
                result.append(
                    str(nums[i]) if i == start else "%s->%s" % (nums[start], nums[i]))
                start = i + 1

        return result


# @lc code=end
