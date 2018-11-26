def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    x_bit = []
    len = 0
    x_rev = 0

    if x > 0 :
        while x > 0 :
            x_bit.append(x%10)
            x = x//10
            len = len + 1
        for i in x_bit:
            len = len - 1
            x_rev = x_rev + i*(10**len)  
        if x_rev <= (2**31)-1:
            return x_rev
        else:
            return 0

    if x < 0 :
        x = -x
        while x > 0 :
            x_bit.append(x%10)
            x = x//10
            len = len + 1
        for i in x_bit:
            len = len - 1
            x_rev = x_rev + i*(10**len)      
        if x_rev <= (2**31):
            return -x_rev
        else:
            return 0
    if x == 0:
        return 0        