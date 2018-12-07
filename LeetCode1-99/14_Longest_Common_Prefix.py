class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ''
        else:    
            output = strs[0]
            for s in strs:
                s=s[:len(output)]
                while s.count(output)==0:
                    output = output[:-1]
                    s=s[:len(output)]                    
                    if len(output)==0:
                        return ''
            return output