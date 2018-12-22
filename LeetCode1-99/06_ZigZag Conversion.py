class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1 or len(s)<=numRows:
            return s
        opt = []
        for i in range(numRows):
            opt.append([s[i]])
        direction_up = True
        layer = numRows-1
        for i in range(numRows,len(s)):
            if direction_up:
                layer -= 1
                if layer == 0:
                    direction_up = False
                opt[layer].append(s[i])
            else:
                layer += 1
                if layer == numRows-1:
                    direction_up = True
                opt[layer].append(s[i])
        for i in range(numRows):
            opt[i] = ''.join(opt[i])
        opt = ''.join(opt)
        return opt