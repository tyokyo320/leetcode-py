#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        item = []
        res_set = []

        sorted(nums)
        result.append(item)
        self.generate(0, nums, item, result)

        for i in result:
            sort_list = sorted(i)
            if sort_list not in res_set:
                res_set.append(sort_list)

        return res_set
    
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

