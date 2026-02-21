class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n=len(edges)
        def bfs(start):
            dist={}
            queue = deque([(start, 0)])
            while queue:
                node,d=queue.popleft()
                if node in dist:
                    continue
                dist[node]=d
                nei = edges[node]
                if nei!=-1:
                    queue.append((nei,d+1))
            return dist
        dist1=bfs(node1)
        dist2=bfs(node2)
        answer=-1
        min_dist=float('inf')
        for i in range(n):
            if i in dist1 and i in dist2:
                max_dist=max(dist1[i],dist2[i])
                if max_dist<min_dist:
                    min_dist=max_dist
                    answer=i
        return answer

        #t.c->o(n)
        #s.c->o(n)
