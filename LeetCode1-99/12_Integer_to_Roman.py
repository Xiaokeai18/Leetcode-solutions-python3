class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        opt = ""
        while num >= 1000:
            num -= 1000
            opt += 'M'
        if num >= 900:
            num -= 900
            opt += 'CM'
        elif num >= 500:
            num -= 500
            opt += 'D'
        if num >= 400:
            num -= 400
            opt += 'CD'
        while num >= 100:
            num -= 100
            opt += 'C'
        if num >= 90:
            num -= 90
            opt += 'XC'
        elif num >= 50:
            num -= 50
            opt += 'L'   
        if num >= 40:
            num -= 40
            opt += 'XL'
        while num >= 10:
            num -= 10
            opt += 'X'  
        if num >= 9:
            num -= 9
            opt += 'IX'
        elif num >= 5:
            num -= 5
            opt += 'V'         
        if num >= 4:
            num -= 4
            opt += 'IV'
        while num >= 1:
            num -= 1
            opt += 'I'    
        return opt