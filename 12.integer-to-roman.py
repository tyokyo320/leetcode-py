#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        # dictionary:
        # key: decimal value as base
        # value: corresponding roman symbol
        mapping_table = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

        roman_string = ''

        # represent input num in roman number system
        for base, roman_symbol in mapping_table.items():

            # update roman string with corresponding roman symbol
            roman_string += (num // base) * roman_symbol

            # update num as remainder
            num = num % base

        return roman_string
# @lc code=end
