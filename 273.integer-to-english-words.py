#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#

from typing import List

# @lc code=start


class Solution:

    def __init__(self):
        self.mapping_table = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen",
            20: "twenty",
            30: "thirty",
            40: "forty",
            50: "fifty",
            60: "sixty",
            70: "seventy",
            80: "eighty",
            90: "ninety",
            100: "hundred",
            1000: "thousand",
            1000000: "million",
            1000000000: "billion"
        }

        self.result = []

    def numberToWords(self, num: int) -> str:
        '''
        6,789(six thousand seven hundred  eighty nine) -> 9 + 80 + 700 + 6000

        divmod(6789, 1000) -> (6, rem: 789)
        '''

        if num == 0:
            return 'Zero'

        for i in range(0, len(str(num)), 3):
            # 从最后3位数字开始获取
            num, rem = divmod(num, 1000)
            if rem:
                if i >= 3:
                    self.result.append(self.mapping_table[10**i])
                self.result.extend(self.getHundreds(rem))

        # print(self.result)
        return ' '.join(self.result[::-1]).title()

    # 获取 10**2 以下的数字
    def getTen(self, num: int) -> List[str]:
        '''
        89(eighty nine) -> 9 + 80

        divmod(89, 10) -> (8, rem: 9) -> divmod(8, 10) -> (0, rem: 8)

        rem -> 8 * 10**1 + 9

        ['nine', 'eighty']
        '''
        result = []
        if num:
            # 数字20以内，直接获取
            if num <= 20:
                result.append(self.mapping_table[num])
            else:
                # 数字大于20小于10**2，按照个位，十位的顺序获取
                for i in range(2):
                    num, rem = divmod(num, 10)
                    if rem:
                        result.append(self.mapping_table[rem*10**i])

        return result

    # 获取 10**3 以下的数字
    def getHundreds(self, num: int) -> List[str]:
        '''
        789(seven hundred eighty nine) -> 9 + 80 + 700

        divmod(789, 100) -> (7, rem: 89)

        ['nine', 'eighty', 'hundred', 'seven']
        '''
        result = []
        num, rem = divmod(num, 100)

        # 取十位和个位
        result.extend(self.getTen(rem))
        # 取百位数
        if num:
            result.append(self.mapping_table[100])
            result.append(self.mapping_table[num])
        return result

# @lc code=end
