class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n=len(passingFees)
        import collections
        graph=collections.defaultdict(list)
        for u,v,t in edges:
            graph[u].append((v,t))
            graph[v].append((u,t))
        best_time=[float('inf')]*n
        best_time[0]=0
        heap=[(passingFees[0],0,0)]
        while heap:
            cost,node,time=heapq.heappop(heap)
            if node==n-1:
                return cost
            for nei,t in graph[node]:
                new_time=time+t
                if new_time<=maxTime and new_time<best_time[nei]:
                    best_time[nei]=new_time
                    heapq.heappush(heap,(cost+passingFees[nei],nei,new_time))
        return -1
        