class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profile = 0
        for i in range(len(prices)-1):
            if prices[i+1] - prices[i] > 0:
                profile += prices[i+1] - prices[i]
        return profile