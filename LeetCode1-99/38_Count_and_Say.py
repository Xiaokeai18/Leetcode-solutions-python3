class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        s = self.countAndSay(n-1) + '*'
        out, count = '', 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count += 1
            else:
                out += str(count) + str(s[i])
                count = 1
        return out