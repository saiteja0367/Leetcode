class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        INF = float('inf')
    
        # dist[node][0] → last edge red
        # dist[node][1] → last edge blue
        dist = [[INF, INF] for _ in range(n)]
        
        dist[0][0] = 0
        dist[0][1] = 0
        
        for _ in range(2*n):
            temp = [row[:] for row in dist]
            
            # relax red edges (must come from blue)
            for u, v in redEdges:
                if dist[u][1] != INF:
                    temp[v][0] = min(temp[v][0], dist[u][1] + 1)
            
            # relax blue edges (must come from red)
            for u, v in blueEdges:
                if dist[u][0] != INF:
                    temp[v][1] = min(temp[v][1], dist[u][0] + 1)
            
            dist = temp
        
        ans = []
        for r, b in dist:
            best = min(r, b)
            ans.append(-1 if best == INF else best)
        
        return ans
            

            