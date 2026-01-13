class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        import collections,heapq
        graph = collections.defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        visited=set()
        dist={i:float('inf') for i in range(1,n+1)}
        dist[n] = 0
        minheap = [(0, n)]
        while minheap:
            d,u=heapq.heappop(minheap)
            if d>dist[u]:
                continue
            for v,w in graph[u]:
                if d+w<dist[v]:
                    dist[v]=d+w
                    heapq.heappush(minheap,(dist[v],v))
        nodes=sorted(range(1,n+1),key=lambda x:dist[x])
        dp={i:0 for i in range(1,n+1)}
        dp[n]=1
        for u in nodes:
            for v,_ in graph[u]:
                if dist[u]>dist[v]:
                    dp[u]=(dp[u]+dp[v])%MOD
        return dp[1]