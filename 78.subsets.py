#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        item = []
        result.append(item)
        self.generate(0, nums, item, result)

        return result
    
    def generate(self, i, nums, item, result):
        if i >= len(nums):
            return

        item.append(nums[i])
        # 注意：这里不能写成result.append(item) -> 指针
        # 不然item里面2加进来时候item = [1, 2]，result会变为 result = [[1, 2], [1, 2]]，而不是期望的结果result = [[1], [1, 2]]
        result.append(list(item))

        # item [1,2,3,...., N] 一条分支是有i的
        self.generate(i+1, nums, item, result)
        
        item.pop()
        # item [1,2,3,....,] 另一条分支是没有i的
        self.generate(i+1, nums, item, result)

# @lc code=end

