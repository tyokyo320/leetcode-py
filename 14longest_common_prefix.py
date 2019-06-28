#!/usr/bin/python3

class Solution(object):

    list1 = ["flower","flow","flight"]
    list2 = ["dog","racecar","car"]

    def longestCommonPrefix(self, strs):
        if not strs: return ""
        
        strs.sort()
        s = ""

        for x, y in zip(strs[0], strs[-1]):
            if x == y: s += x
            else: return s
        return s

    def longestCommonPrefix1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        if len(strs) == 0:
            return ""
        m = min(strs, key=len)
        for x in range(len(m)):
            if self.check_index_of_words(strs, x):
                result += strs[0][x]
            else:
                return result
        return result

    def check_index_of_words(self, strs, i):
        temp = strs[0][i]
        for y in strs[1:]:
            if temp != y[i]:
                return False
        return True

if __name__ == "__main__":
    r = Solution()
    result = r.longestCommonPrefix(r.list1)
    print(f"result {result}")