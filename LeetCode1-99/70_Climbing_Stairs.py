class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways = [0,1,2]
        if n > 2:
            for i in range(3,n+1):
                ways.append(ways[i-1]+ways[i-2])
        return ways[n]