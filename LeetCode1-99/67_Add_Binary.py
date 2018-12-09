class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        output = []
        plus = 0
        a=list(a)
        b=list(b)
        if len(a)>len(b):
            for i in range(len(a)-len(b)):
                b.insert(0,'0')
        else:
            for i in range(len(b)-len(a)):
                a.insert(0,'0')
        for i in range(len(a))[::-1]:
            output.insert(0,int(a[i])+int(b[i])+plus)
            if output[0] == 2:
                output[0] = 0
                plus = 1
            elif output[0] == 3:
                output[0] = 1
                plus = 1
            else:
                plus = 0
        if plus == 1:
            output.insert(0,1)
        output = [str(x) for x in output]
        return ''.join(output)