# from collections import deque
# from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # m=len(grid)
        # n=len(grid[0])
        # minutes=0
        # while True:
        #     torot=[]
        #     for i in range(m):
        #         for j in range(n):
        #             if grid[i][j]==1:
        #                 if (i > 0 and grid[i-1][j] == 2) or \
        #                    (i < m-1 and grid[i+1][j] == 2) or \
        #                    (j > 0 and grid[i][j-1] == 2) or \
        #                    (j < n-1 and grid[i][j+1] == 2):
        #                     torot.append((i, j))
        #     if not torot:
        #         break
        #     for i,j in torot:
        #         grid[i][j]=2
        #     minutes+=1
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j]==1:
        #             return -1
        # return minutes

        m=len(grid)
        n=len(grid[0])
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        q=deque()
        fresh=0
        minutes=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        while q and fresh>0:
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    newrow=r+dr
                    newcol=c+dc
                    if 0<=newrow<m and 0<=newcol<n and grid[newrow][newcol]==1:
                        grid[newrow][newcol]=2
                        fresh-=1
                        q.append((newrow,newcol))
            minutes+=1
        return minutes if fresh==0 else -1




