class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
            graph = {i: [] for i in range(n)}
            indegree = [0] * n
            for u,v in edges:
                graph[u].append(v)
                indegree[v]+=1
            ancestors = [set() for _ in range(n)]
            def bfs():
                q=deque()
                for i in range(n):
                    if indegree[i]==0:
                        q.append(i)
                while q:
                    curr=q.popleft()
                    for nei in graph[curr]:
                        #adding direct parent
                        ancestors[nei].add(curr)
                        #adding all the ansectors of parent
                        ancestors[nei].update(ancestors[curr])
                        indegree[nei]-=1
                        if indegree[nei]==0:
                            q.append(nei)
            bfs()
            return [sorted(list(a)) for a in ancestors]
            #t.c->o(n2)
            #s.c->o(n2)
        