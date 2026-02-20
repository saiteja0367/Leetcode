class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # adj=defaultdict(list)
        # for v1,v2,dist in edges:
        #     adj[v1].append((v2,dist))
        #     adj[v2].append((v1,dist))
        # def dijkstra(src):
        #     dist=[float('inf')]*n
        #     dist[src]=0
        #     heap=[(0,src)] #heap contains distance and node
        #     while heap:
        #         curr_dist,node=heapq.heappop(heap)
        #         if curr_dist>dist[node]:
        #             continue
        #         for nei,weight in adj[node]:
        #             new_dist=curr_dist+weight
        #             if new_dist<dist[nei]:
        #                 dist[nei]=new_dist
        #                 heapq.heappush(heap, (new_dist, nei))
        #     return dist
        # min_reachable=float('inf')
        # answer=-1
        # for city in range(n):
        #     distances=dijkstra(city)
        #     reachable=0
        #     for d in distances:
        #         if d<=distanceThreshold:
        #             reachable+=1
        #     reachable-=1
        #     #we have to break the tie based on larger index
        #     if reachable<=min_reachable:
        #         min_reachable=reachable
        #         answer=city
        # return answer

        # #t.c->o(n*Elogn)
        # #s.c->o(E+n)




        #now i will do it with floyd-warshall algorithm
        INF=float('inf')
        dist=[[INF] * n for _ in range(n)]
        for i in range(n):
            dist[i][i]=0
        for u,v,w in edges:
            dist[u][v]=w
            dist[v][u]=w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k]+dist[k][j]<dist[i][j]:
                        dist[i][j]=dist[i][k]+dist[k][j]
        min_reachable=float('inf')
        answer=-1
        for city in range(n):
            reachable=0
            for neighbor in range(n):
                if city!=neighbor and dist[city][neighbor]<=distanceThreshold:
                    reachable+=1
            if reachable<=min_reachable:
                min_reachable=reachable
                answer=city
        return answer


        #t.c->o(n3)
        #s.c->o(n2)