class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n=len(favorite)
        indegree=[0]*n
        for i in range(n):
            indegree[favorite[i]]+=1
        queue=deque()
        depth=[1]*n
        for i in range(n):
            if indegree[i]==0:
                queue.append(i)
        while queue:
            node=queue.popleft()
            nxt=favorite[node]
            depth[nxt]=max(depth[nxt],depth[node]+1)
            indegree[nxt]-=1
            if indegree[nxt]==0:
                queue.append(nxt)
        visited=[False]*n
        max_cycle=0
        two_cycle_sum=0
        for i in range(n):
            if indegree[i]>0 and not visited[i]:
                cycle_length=0
                node=i
                while not visited[node]:
                    visited[node]=True
                    node=favorite[node]
                    cycle_length+=1
                if cycle_length==2:
                    a=i
                    b=favorite[i]
                    two_cycle_sum+=depth[a]+depth[b]
                else:
                    max_cycle=max(max_cycle,cycle_length)
        return max(max_cycle,two_cycle_sum)

        #t.c->o(n)
        #s.c->o(n)
        