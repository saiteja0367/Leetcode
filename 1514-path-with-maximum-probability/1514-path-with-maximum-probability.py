class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph=collections.defaultdict(list)
        for i,(u,v) in enumerate(edges):
            graph[u].append((v,succProb[i]))
            graph[v].append((u,succProb[i]))
        heap=[(-1.0,start_node)]
        visited=set()
        while heap:
            prob,node=heapq.heappop(heap)
            prob =-prob
            if node==end_node:
                return prob
            if node in visited:
                continue
            visited.add(node)
            for (next_node,edge_prob) in graph[node]:
                new_prob=prob*edge_prob
                heapq.heappush(heap, (-new_prob,next_node))
        return 0.0

        