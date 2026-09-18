class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        squares = [[] for _ in range(9)]
        for col in range(0,9):
            for row in range(0, 9):
                numberstr = board[col][row]
                if numberstr == ".":
                    continue
                squareindex = col // 3 + 3*(row//3)
                if numberstr in rows[row]:
                    return False
                if numberstr in cols[col]:
                    return False
                if numberstr in squares[squareindex]:
                    return False
                rows[row].append(numberstr)
                cols[col].append(numberstr)
                squares[squareindex].append(numberstr)
        return True
