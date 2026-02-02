class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()
        q = deque()
        #finding the 1st phase of island
        found = False
        for r in range(n):
            if found:
                break
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))
                    visited.add((r, c))
                    found = True
                    break
        #with the help of 1st phase we will mark the entire island
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    if grid[nr][nc] == 1 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))
        q=deque(visited)
        res = 0
        while q:
            for _ in range(len(q)): 
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                        if grid[nr][nc] == 1:
                            return res
                        visited.add((nr, nc))
                        q.append((nr, nc))
            res += 1
        return -1
