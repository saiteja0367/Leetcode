class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n=len(edges)
        indegree=[0]*n
        for i in range(n):
            if edges[i]!=-1:
                indegree[edges[i]]+=1
        queue=deque()
        for i in range(n):
            if indegree[i]==0:
                queue.append(i)
        max_len=float('inf')
        while queue:
            node=queue.popleft()
            nxt=edges[node]
            if nxt != -1:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        visited=[False]*n
        max_len=-1
        for i in range(n):
            if indegree[i]>0 and not visited[i]:
                curr=i
                cycle_len=0
                while not visited[curr]:
                    visited[curr]=True
                    curr=edges[curr]
                    cycle_len+=1
                    max_len=max(max_len,cycle_len)
        return max_len

        #t.c->o(n)
        #s.c->o(n)