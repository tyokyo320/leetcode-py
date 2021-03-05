#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        此题注意审题，题目意思是找到是否存在两个不重复的索引i，j，满足nums[i] == nums[j]，同时i与j之间的距离在k以内
        '''
        hashmap = {}
        for i, j in enumerate(nums):
            if j in hashmap and i - hashmap[j] <= k:
                return True
            else:
                hashmap[j] = len(hashmap)
        return False
# @lc code=end

