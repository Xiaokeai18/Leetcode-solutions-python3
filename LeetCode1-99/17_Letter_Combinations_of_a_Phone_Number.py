class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.dic = {'2':['a','b','c'],'3':['d','e','f'],
            '4': ['g', 'h', 'i'],'5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],'7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],'9': ['w', 'x', 'y', 'z']}
        self.output = []
        if digits:
            self.backtrack(digits,"")
        return self.output

    def backtrack(self,digits,string):
        if not digits:
            self.output.append(string)
        else:
            for letter in self.dic[digits[0]]:
                self.backtrack(digits[1:],string+letter)