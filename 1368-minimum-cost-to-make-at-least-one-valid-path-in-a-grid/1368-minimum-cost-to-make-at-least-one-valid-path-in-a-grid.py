class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        dirs={1:[0,1],
        2:[0,-1],
        3:[1,0],
        4:[-1,0]}
        rows=len(grid)
        cols=len(grid[0])
        dq = deque()
        dq.append((0,0,0))
        min_cost={(0,0):0}
        while dq:
            r,c,cost=dq.popleft()
            if (r,c)==(rows-1,cols-1):
                return cost
            for d in dirs:
                dr,dc=dirs[d]
                nr=r+dr
                nc=c+dc
                if 0<=nr<rows and 0<=nc<cols:
                    if d==grid[r][c]:
                        n_cost=cost
                    else:
                        n_cost=cost+1
                    if (nr,nc) not in min_cost or n_cost <min_cost[(nr,nc)]:
                        min_cost[(nr,nc)]=n_cost
                        if d==grid[r][c]:
                            dq.appendleft((nr,nc,n_cost))
                        else:
                            dq.append((nr,nc,n_cost))
        return -1



        