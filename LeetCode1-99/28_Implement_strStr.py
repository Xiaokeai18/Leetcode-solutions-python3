class Solution:
    def strStr(self,haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == []:
            return 0
        elif len(haystack) >= len(needle):
            print(range(len(haystack)-len(needle)+1))
            for i in range(len(haystack)-len(needle)+1):
                print(haystack[i:i+len(needle):1])
                if haystack[i:i+len(needle):1] == needle:
                    return i
            return -1
        else:
            return -1

