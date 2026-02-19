class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

    #we have used bellmanford but this is slow because there might be cycle    exist in the problem and each node has two states

    #     INF = float('inf')
    #     dist = [[INF, INF] for _ in range(n)]
    #     dist[0][0] = 0
    #     dist[0][1] = 0
    #     for _ in range(2*n):
    #         temp = [row[:] for row in dist]
    #         for u, v in redEdges:
    #             if dist[u][1] != INF:
    #                 temp[v][0] = min(temp[v][0], dist[u][1] + 1)
    #         for u, v in blueEdges:
    #             if dist[u][0] != INF:
    #                 temp[v][1] = min(temp[v][1], dist[u][0] + 1)
    #         dist = temp  
    #     ans = []
    #     for r, b in dist:
    #         best = min(r, b)
    #         ans.append(-1 if best == INF else best) 
    #     return ans

    #    #t.c->O(nE)
    #    #s.c-.O(n)

    #now we will go with bfs
    #here i am considering '0' as red and '1' as blue
        graph={i:[[],[]] for i in range(n)}
        for u,v in redEdges:
            graph[u][0].append(v)
        for u,v in blueEdges:
            graph[u][1].append(v)
        res=[-1]*n
        res[0]=0
        queue=deque()
        #we will be starting with both color states
        queue.append((0,0))
        queue.append((0,1))
        visited=set()
        visited.add((0,0))
        visited.add((0,1))
        steps=0
        while queue:
            size=len(queue)
            for _ in range(size):
                node,last_color=queue.popleft()
                if res[node]==-1:
                    res[node]=steps
                next_color=1-last_color
                for neighbor in graph[node][next_color]:
                    if (neighbor,next_color) not in visited:
                        visited.add((neighbor,next_color))
                        queue.append((neighbor,next_color))
            steps+=1
        return res

        #t.c->o(n+e)
        #s.c->o(n+e)


                

                