class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        r=len(heights)
        c=len(heights[0])
        visit=set()
        min_heap=[(0,0,0)] #we are taking the effort , row, col
        while min_heap:
            effort,i,j=heapq.heappop(min_heap)
            if (i,j) in visit:
                continue
            visit.add((i,j))
            if i==r-1 and j==c-1:
                return effort
            directions=[(1,0), (-1,0), (0,1), (0,-1)]
            for di,dj in directions:
                ni=i+di
                nj=j+dj
                if 0<=ni<r and 0<=nj<c:
                    diff=abs(heights[ni][nj]-heights[i][j])
                    new_effort=max(effort,diff)
                    heapq.heappush(min_heap,(new_effort,ni,nj))
        #t.c->o(mnlog(mn))
        #s.c->o(mn)


        