#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
        方法1：去掉列表中的数字之间逗号，转为int，然后+1后再转换回去
        
        temp_str = ','.join(str(i) for i in digits)
        num_str = temp_str.replace(',', '')
        num = int(num_str) + 1

        num_str = str(num)

        temp_result = num_str.split()
        result = []
        for i in temp_result[0]:
            result.append(int(i))

        return result
        '''

        '''
        方法1的其他写法1：
        a = ''.join(map(str, digits))
        b = int(a) + 1
        c = str(b)
        return list(map(int, c))
        '''

        '''
        方法1的优化写法2：
        return list(map(int, str(int(''.join(map(str, digits))) + 1)))
        '''

        '''
        方法2：
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, len(digits) - 1 - i)
        return [int(i) for i in str(num+1)]
        '''

        '''
        方法2：其他写法
        '''
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        
        digits.insert(0, 1)
        return digits

# @lc code=end

