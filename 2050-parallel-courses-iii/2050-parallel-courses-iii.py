class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        prereqMap = {i: [] for i in range(n)}
        indegree = [0] * (n)
        for u,v in relations:
            u-=1
            v-=1
            prereqMap[u].append(v)
            indegree[v]+=1
        def bfs():
            q=deque()
            ind=indegree[:]
            dist=[0]*n
            for i in range(n):
                if ind[i]==0:
                    q.append(i)
                    dist[i]=time[i]
            while q:
                curr=q.popleft()
                for nei in prereqMap[curr]:
                    dist[nei]=max(dist[nei],dist[curr]+time[nei])
                    ind[nei]-=1
                    if ind[nei]==0:
                        q.append(nei)
            return max(dist)
        return bfs()