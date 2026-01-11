class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph=collections.defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v,w+1))
            graph[v].append((u,w+1))
        dist={0:0}
        minheap=[(0,0)] #(distance, node)
        while minheap:
            d,node=heapq.heappop(minheap)
            if d>dist[node]:
                continue
            for nei,cost in graph[node]:
                new_dist=d+cost
                if new_dist<dist.get(nei,float('inf')) and new_dist<=maxMoves:
                    dist[nei]=new_dist
                    heapq.heappush(minheap,(new_dist,nei))
        result=len(dist)
        for u,v,w in edges:
            moves_u=max(0,maxMoves-dist.get(u,maxMoves+1))
            moves_v=max(0,maxMoves-dist.get(v,maxMoves+1))
            result+=min(w,moves_u+moves_v)
        return result
