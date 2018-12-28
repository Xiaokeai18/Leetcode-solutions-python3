#这个题目坑很多，详情可见issue
import math
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        #根据杨辉三角的性质容易得到，每行的数据其实是组合数
        opt = []
        for i in range(rowIndex+1):
            opt.append(self.combinatorial(rowIndex,i))
        return opt

    def combinatorial(self,n,i):
        #计算组合数
        comb = math.factorial(n)/(math.factorial(n-i)*math.factorial(i))
        return int(comb)    #python3中没有long函数，int表示长整型；python2中有long