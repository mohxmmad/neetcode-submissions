class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            hashmap = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in hashmap:
                        return False
                    else:
                        hashmap.add(board[i][j])
            hashmap.clear()
        
        for i in range(9):
            hashmap = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in hashmap:
                        return False
                    else:
                        hashmap.add(board[j][i])
            hashmap.clear()
        x = 0
        y = 0

        for k in range(9):
            hashmap = set()
            for i in range(x, x+3):
                for j in range(y, y+3):
                    if board[i][j] != ".":
                        if board[i][j] in hashmap:
                            return False
                        else:
                            hashmap.add(board[i][j])
            hashmap.clear()

            y += 3
            y = y%9
            
            if k > 5:
                x = 6
            elif k > 2:
                x = 3
            else:
                x = 0
        
        return True
