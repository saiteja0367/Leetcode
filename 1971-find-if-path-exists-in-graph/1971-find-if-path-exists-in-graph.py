class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited=set()
        def dfs(source,destination):
            if source==destination:
                return True
            visited.add(source)
            for neighbor in graph[source]:
                if neighbor not in visited:
                    if dfs(neighbor,destination):
                        return True
            return False
        return dfs(source,destination)