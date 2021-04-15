#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0

        # 设置flag
        nums = [None] * n
        nums[0] = False
        nums[1] = False

        for i in range(n):
            if nums[i] == None:
                nums[i] = True
                # 找到第一个质数后，以它为倍数的数字全部设置为False
                for j in range(i + i, n, i):
                    nums[j] = False

        return sum(nums)


# @lc code=end
