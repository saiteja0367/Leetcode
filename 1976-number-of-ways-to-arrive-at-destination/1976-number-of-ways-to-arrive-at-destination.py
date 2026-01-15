class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD=10**9+7
        import collections
        graph=collections.defaultdict(list)
        for u,v,t in roads:
            graph[u].append((v,t))
            graph[v].append((u,t))
        best_time = [float('inf')] * n
        best_time[0] = 0
        ways=[0]*n
        ways[0]=1
        heap=[(0,0)] #starting time and node
        while heap:
            time,node=heapq.heappop(heap)
            if time>best_time[node]:
                continue
            for nei,t in graph[node]:
                new_time=time+t
                if new_time<best_time[nei]:
                    best_time[nei]=new_time
                    ways[nei]=ways[node]
                    heapq.heappush(heap,(new_time,nei))
                elif new_time==best_time[nei]:
                    ways[nei] = (ways[nei] + ways[node]) % MOD
                else:
                    pass
        return ways[n-1]%MOD
                    

        