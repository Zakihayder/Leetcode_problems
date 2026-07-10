class Solution(object):
    def gameOfLife(self, board):
        
        rows = len(board)
        cols = len(board[0])

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for i in range(rows):
            for j in range(cols):

                live = 0

                for dr, dc in directions:
                    r = i + dr
                    c = j + dc

                    if 0 <= r < rows and 0 <= c < cols:
                        if board[r][c] == 1 or board[r][c] == 2:
                            live += 1

                if board[i][j] == 1:
                    if live < 2 or live > 3:
                        board[i][j] = 2      # Alive -> Dead

                else:
                    if live == 3:
                        board[i][j] = 3      # Dead -> Alive

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1