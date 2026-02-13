class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n=len(bombs)
        graph = {i: [] for i in range(n)}
        for i in range(n):
            x1,y1,r1=bombs[i]
            for j in range(n):
                if i==j:
                    continue
                x2,y2,_=bombs[j]
                dx=x1-x2
                dy=y1-y2
                if dx*dx+dy*dy<=r1*r1:
                    graph[i].append(j)
        def bfs(start):
            visited=set()
            queue=deque([start])
            visited.add(start)
            while queue:
                node=queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            return len(visited)
        max_den=0
        for i in range(n):
            max_den=max(max_den,bfs(i))
        return max_den

        #t.c->o(n3)
        #s.c->O(n²)



        