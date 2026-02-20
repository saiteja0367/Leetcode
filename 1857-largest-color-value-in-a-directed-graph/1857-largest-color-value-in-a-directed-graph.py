class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n=len(colors)
        adj=defaultdict(list)
        indegree = [0] * n
        for u,v in edges:
            adj[u].append(v)
            indegree[v]+=1
        dp=[[0]*26 for _ in range(n)]
        queue = deque()
        for i in range(n):
            if indegree[i]==0:
                queue.append(i)
        processed=0
        result=0
        while queue:
            node=queue.popleft()
            processed+=1
            color_index=ord(colors[node])-ord('a')
            dp[node][color_index]+=1
            result=max(result,dp[node][color_index])
            for nei in adj[node]:
                for c in range(26):
                    dp[nei][c]=max(dp[nei][c],dp[node][c])
                indegree[nei]-=1
                if indegree[nei]==0:
                    queue.append(nei)
        if processed<n:
            return -1
        return result

        #t.c->O((V + E) * 26)
        #s.c->O(V * 26)
        

        
        