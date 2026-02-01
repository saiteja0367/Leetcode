class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        visited=[False]*n
        mindist=[inf]*n
        pq=[]
        heapq.heappush(pq,(0,0))
        mindist[0]=0
        totalcost=0
        while pq:
            cost,u=heapq.heappop(pq)
            if visited[u]:
                continue
            visited[u]=True
            totalcost+=cost
            x1,y1=points[u]
            for v in range(n):
                if not visited[v]:
                    x2,y2=points[v]
                    d=abs(x1-x2)+abs(y1-y2)
                    if d<mindist[v]:
                        mindist[v]=d
                        heapq.heappush(pq,(d,v))
        return totalcost
