
#https://leetcode.com/problems/valid-sudoku/submissions/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_hash = collections.defaultdict(set)
        for i in range(len(board)):
            row_hash = set()
            col_hash = set()
            for j in range(len(board[i])):
                if board[i][j] in row_hash and board[i][j] != ".":
                    return False
                row_hash.add(board[i][j])

                if board[j][i] in col_hash and board[j][i] != ".":
                    return False
                col_hash.add(board[j][i])

                if board[i][j] in box_hash[(i // 3, j // 3)] and board[i][j] != ".":
                    return False
                box_hash[(i // 3, j // 3)].add(board[i][j])

        return True
