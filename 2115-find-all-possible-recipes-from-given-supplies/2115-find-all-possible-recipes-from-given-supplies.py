class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph=defaultdict(list)
        indegree={}
        for i in range(len(recipes)):
            recipe=recipes[i]
            indegree[recipe]=len(ingredients[i])
            for ing in ingredients[i]:
                graph[ing].append(recipe)
        def bfs():
            q=deque(supplies)
            ind=indegree.copy()
            res=[]
            while q:
                curr=q.popleft()
                for nei in graph[curr]:
                    indegree[nei]-=1
                    if indegree[nei]==0:
                        q.append(nei)
                        res.append(nei)
            return res
        return bfs()
