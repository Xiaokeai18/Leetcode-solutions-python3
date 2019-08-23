class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        
        if length <= 1:
            return s
        dp = [[]]
        maxpa = 0
        output = s[0]
        for right in range(1,length):
            dp.append([])
            for left in range(right):
                if s[left] == s[right] and (right-left<=2 or dp[right-1][left+1]):
                    dp[right].append(True)
                    palindromic = right - left
                    if palindromic > maxpa:
                        maxpa = palindromic
                        output = s[left:right+1]
                else:
                    dp[right].append(False)
        return output                
