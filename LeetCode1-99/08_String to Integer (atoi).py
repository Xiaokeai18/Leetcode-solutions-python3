class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        num = ""
        for i in str:
            if i == ' ':
                if num == "":
                    continue
                else: 
                    break
            elif i == '+' or i == '-':
                if num == "":
                    num += i
                else:
                    break
            elif i >= '0' and i <= '9':
                num += i
            else:
                break
        if num == "" or num == "+" or num == "-":
            return 0
        else:
            return min(max(int(num),-2147483648),2147483647)