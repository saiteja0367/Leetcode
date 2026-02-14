class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree=[0]*n
        connections=set()
        for u,v in roads:
            degree[u]+=1
            degree[v]+=1
            connections.add((u,v))
            connections.add((v,u))
        max_rank=0
        for i in range(n):
            for j in range(i+1,n):
                rank=degree[i]+degree[j]
                if (i,j) in connections:
                    rank-=1
                max_rank=max(max_rank,rank)
        return max_rank


        #t.c->O(n² + E)
        #s.c->O(n + E)
