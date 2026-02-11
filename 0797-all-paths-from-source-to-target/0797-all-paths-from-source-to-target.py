class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res=[]
        target=len(graph)-1
        def dfs(node,path):
            if node==target:
                res.append(list(path))
                return
            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor,path)
                path.pop()
        dfs(0,[0])
        return res

        