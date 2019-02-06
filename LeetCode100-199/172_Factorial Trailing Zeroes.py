class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        opt = 0
        i = 1
        while 5**i<=n:
            opt += int(n/(5**i))
            i += 1
        return opt