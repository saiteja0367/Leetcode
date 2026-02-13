class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph={}
        for i in range(len(rooms)):
            graph[i]=rooms[i]
        visited=set()
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        dfs(0)
        return len(visited)==len(rooms)


        #t.c->o(n+e)~=o(n)
        #s.c->o(n)
                


        