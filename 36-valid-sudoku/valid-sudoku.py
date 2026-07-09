import numpy as np
class Solution(object):
    def isValidSudoku(self, board):

        seen = ""
        seen1 = ""
        seen2 = ""
        board1 = np.transpose(board)
        board2 = np.transpose(board1)
        board2 = board2.reshape(3, 3, 3, 3).transpose(0, 2, 1, 3).reshape(9, 9)

        for i in range(9):
            for j in range(9):
                if str(board[i][j]) in seen and board[i][j].isalnum():
                    return False
                else:
                    seen += str(board[i][j])

                if str(board1[i][j]) in seen1 and board1[i][j].isalnum():
                    return False
                else:
                    seen1 += str(board1[i][j])
                
                if str(board2[i][j]) in seen2 and board2[i][j].isalnum():
                    return False
                else:
                    seen2 += str(board2[i][j])
            seen = ""
            seen1 = ""
            seen2 = ""

        return True
        
        