class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def isValid(lst):
            """
            type lst: List
            """
            dic = {}
            for i in lst:
                if i != ".":
                    if i in dic:
                        return False
                    else:
                        dic[i] = 1
            return True
        for lst in board:
            if not isValid(lst):
                return False
        for i in range(9):
            test_lst = []
            for j in range(9):
                test_lst.append(board[j][i])
            if not isValid(test_lst):
                return False
        for i in (0,3,6):
            for j in (0,3,6):
                test_lst = []
                for nums in board[i][j:j+3]:
                    test_lst.append(nums)
                for nums in board[i+1][j:j+3]:
                    test_lst.append(nums)
                for nums in board[i+2][j:j+3]:
                    test_lst.append(nums)
                if not isValid(test_lst):
                    return False
        return True
