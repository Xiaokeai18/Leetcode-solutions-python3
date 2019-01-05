class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        character = 'abcdefghijklmnopqrstuvwxyz0123456789'
        l = []
        for i in s:
            if i in character:
                l.append(i)
        if l == l[::-1]:
            return True
        return False