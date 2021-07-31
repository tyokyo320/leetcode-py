#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start

import itertools


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        方法1：引用itertools

        letter_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        if len(digits) == 0:
            return []

        result = []
        for i in digits:
            result.append(letter_map[i])

        # 从二维列表中的子列表中选出一个元素相加，列出所有组合
        return [''.join(i) for i in itertools.product(*result)]
        '''

        '''
        方法2：bfs，先把2的全列出(a, b, c)，再把3的全列出(d, e, f)，最后将2个组合

        if not digits:
            return []
        res = [""]
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        for digit in digits:
            res = [m + n for m in res for n in d[digit]]
        return res
        '''

        '''
        方法3：dfs，直接列完一个字母的组合(ad, ae, af)
        '''

        result = []
        if not digits:
            return []

        self.dfs(digits, 0, "", result)
        return result

    def dfs(self, digits, index, temp, result):
        '''
        eg.input = 23
        dfs：a -> ad -> a -> ae -> a -> af -> ....
        '''
        digit_mapping = {
            0: "",
            1: "",
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        # 停止条件（输入23的情况，第一次当index等于2说明temp等于ad，将结果放入result中，退回a，让a继续尝试ae等）
        if index == len(digits):
            result.append(temp)
            return

        # 获取输入的一位数（输入为23的情况，先2）
        digit = int(digits[index])
        # 获取2对应的字母（abc）
        letters = digit_mapping[digit]
        for i in range(len(letters)):
            # index来控制输入的数字（23）
            # 这里index+1是为了向下递归时候选择（index+1后 a变为ad，然后判断此时index=2=ad的长度，然后退回到a）
            self.dfs(digits, index+1, temp+letters[i], result)

# @lc code=end
