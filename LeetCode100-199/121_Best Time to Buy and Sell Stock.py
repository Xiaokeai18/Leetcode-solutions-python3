class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        opt = 0
        minimum = float("inf")
        for price in prices:
            if minimum>=price:
                minimum = price
            else:
                opt = max(opt,price-minimum)
        return opt