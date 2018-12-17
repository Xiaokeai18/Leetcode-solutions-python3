class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = max_len = 0
        hash = {}      
        for i in range(len(s)):
            if s[i] in hash and start <= hash[s[i]]:
                start = hash[s[i]] + 1
            else:
                max_len = max(max_len, i - start + 1)
            hash[s[i]] = i
            
        return max_len
