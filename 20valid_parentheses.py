class Solution1(object):
    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {
            ")": "(", 
            "}": "{", 
            "]": "["
        }

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#' 
                # if stack:
                #     top_element = stack.pop()
                # else:
                #     top_element = "#"

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: return True
        
        if s[0] in ")]}":
            return False

        s = list(s)
        # print(list(s))
        index = 0
        while index <= len(s) - 1:
            # print(f"index {index} {len(s) - 1}")
            if s[index] in "([{":
                index += 1
                continue
            else:
                if s[0] in ")]}":
                    return False
                if abs(ord(s[index]) - ord(s[index-1])) < 3:
                    del s[index]
                    index -= 1
                    del s[index]
                    index -= 1
            # print(s)
            index += 1
        # print(s)
        if not s:
            return True
        else:
            return False


if __name__ == "__main__":
    test_data = ["((()))", "((()", "))", "{}][}}{[))){}{}){(}]))})[({", ")", "{{)}"]
    while test_data:
        item = test_data.pop()
        result = Solution().isValid(item)
        print(result)
