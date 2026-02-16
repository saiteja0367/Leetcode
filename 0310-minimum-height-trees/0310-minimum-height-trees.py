class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #we will handle the single node
        if n==1:
            return [0]
        #we will build the graph and degree array
        graph=defaultdict(list)
        degree=[0]*n
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u]+=1
            degree[v]+=1
        #we will intilaize the leaves means (degree==1)
        q=deque()
        for i in range(n):
            if degree[i]==1:
                q.append(i)
        remaining_nodes=n
        while remaining_nodes>2:
            size=len(q)
            remaining_nodes-=size
            for _ in range(size):
                leaf=q.popleft()
                for neighbor in graph[leaf]:
                    degree[neighbor]-=1
                    if degree[neighbor]==1:
                        q.append(neighbor)
        return list(q)


        #t.c->o(n)
        #s.c->o(n)