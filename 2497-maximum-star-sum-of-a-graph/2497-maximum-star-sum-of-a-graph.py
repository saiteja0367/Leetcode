class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        n=len(vals)
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(vals[v])
            graph[v].append(vals[u])
        max_sum=float('-inf')
        for i in range(n):
            neighbors=graph[i]
            neighbors=[x for x in neighbors if x>0]
            neighbors.sort(reverse=True)
            star_sum=vals[i]+sum(neighbors[:k])
            max_sum=max(max_sum,star_sum)
        return max_sum

        #t.c->O(nlogn+m)
        #s.c->o(n+m)

        