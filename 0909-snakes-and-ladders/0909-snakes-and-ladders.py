class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        arr = [-1] * (n * n + 1)
        idx = 1
        left_to_right = True
        for r in range(n - 1, -1, -1):
            if left_to_right:
                for c in range(n):
                    arr[idx] = board[r][c]
                    idx += 1
            else:
                for c in range(n - 1, -1, -1):
                    arr[idx] = board[r][c]
                    idx += 1
            left_to_right = not left_to_right
        from collections import deque
        q = deque([(1, 0)])    
        visited = set([1])
        while q:
            curr, moves = q.popleft()
            if curr == n * n:
                return moves
            for dice in range(1, 7):
                nxt = curr + dice
                if nxt > n * n:
                    continue
                if arr[nxt] != -1:
                    nxt = arr[nxt]
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, moves + 1))
        return -1
