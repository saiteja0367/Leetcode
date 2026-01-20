class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])
        dirs = [(-1,-1), (-1,0), (-1,1),
                (0,-1),          (0,1),
                (1,-1),  (1,0),  (1,1)]
        for i in range(m):
            for j in range(n):
                live_count = 0
                for dx, dy in dirs:
                    ni = i + dx
                    nj = j + dy
                    if 0 <= ni < m and 0 <= nj < n:
                        if abs(board[ni][nj]) == 1:
                            live_count += 1
                if board[i][j] == 1:
                    if live_count < 2 or live_count > 3:
                        board[i][j] = -1 
                else:
                    if live_count == 3:
                        board[i][j] = 2
        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
