class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        isPositive = True
        if dividend < 0:
            isPositive = not isPositive
            dividend = -dividend
        if divisor < 0:
            isPositive = not isPositive
            divisor = -divisor
        
        if dividend < divisor:
            return 0
        
        opt,exponent = 0,0
        divisor_1 = divisor
        while dividend-divisor_1>divisor_1:
            divisor_1 <<= 1
            exponent += 1

        opt = (1<<exponent) + self.divide(dividend-divisor_1,divisor)
        if not isPositive:
            opt = -opt
        return min(max(opt,-2147483648),2147483647)