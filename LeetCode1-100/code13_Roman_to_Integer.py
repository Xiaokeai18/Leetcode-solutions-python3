class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        previous = float('inf')
        integer = 0
        for bit in s:
            current = dict[bit]
            if previous < current:
                integer -= 2*previous

            integer += current
            previous = current
        return integer