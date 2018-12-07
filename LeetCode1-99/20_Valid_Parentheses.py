class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        match = {')':'(',']':'[','}':'{'}  
        for element in s:
            if element not in match:
                stack.append(element)
            else:
                if stack == []:
                    return False
                if stack[-1] == match[element]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False