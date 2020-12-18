#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generate("", n, n, result)
        return result

    def generate(self, item, left, right, result):
        # 当左右括号都放光的时候，结果就ok了
        if left == 0 and right == 0:
            result.append(item)
            return

        # 左括号大于0说明还可以继续放左括号
        if left > 0:
            # 左括号放一个，数量-1
            self.generate(item + "(", left - 1, right, result)
        if left < right:
            # 当右括号剩余数量大于左括号，这个时候可以放右括号
            self.generate(item + ")", left, right - 1, result)
# @lc code=end

