class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:          
            x_str = str(x)
            if x_str == x_str[::-1]:
                return True
            else:
                return False