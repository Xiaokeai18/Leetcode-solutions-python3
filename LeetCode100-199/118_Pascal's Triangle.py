class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        opt = []
        for i in range(numRows):
            opt.append([1])
            for k in range(1,len(opt[i-1])):
                opt[i].append(opt[i-1][k]+opt[i-1][k-1])
            if i>0:
                opt[i].append(1)
        return opt