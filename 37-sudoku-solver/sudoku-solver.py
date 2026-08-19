class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    num = board[r][c]
                    box = (r // 3) * 3 + (c // 3)

                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)

        def backtrack(index):
            if index == len(empty):
                return True

            r, c = empty[index]
            box = (r // 3) * 3 + (c // 3)

            for num in "123456789":

                if num in rows[r] or num in cols[c] or num in boxes[box]:
                    continue

                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)

                if backtrack(index + 1):
                    return True

                board[r][c] = '.'
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[box].remove(num)

            return False

        backtrack(0)