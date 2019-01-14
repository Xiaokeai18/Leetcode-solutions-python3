class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        opt = 0
        index = 1
        for i in s:
            opt += (ord(i)-64)*(26**(len(s)-index))
            index += 1
        return opt