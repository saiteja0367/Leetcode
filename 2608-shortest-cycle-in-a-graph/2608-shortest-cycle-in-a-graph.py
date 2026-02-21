class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        min_cycle=float('inf')
        for i in range(n):
            dist=[-1]*n
            parent=[-1]*n
            queue=deque([i])
            dist[i]=0
            while queue:
                node=queue.popleft()
                for nei in adj[node]:
                    if dist[nei]==-1:
                        dist[nei]=dist[node]+1
                        parent[nei]=node
                        queue.append(nei)
                    elif parent[node]!=nei:
                        cycle_len=dist[node]+dist[nei]+1
                        min_cycle=min(min_cycle,cycle_len)
        return min_cycle if min_cycle != float('inf') else -1
        
        #t.c->O(V × (V + E))
        #s.c->O(V × (V + E))
        