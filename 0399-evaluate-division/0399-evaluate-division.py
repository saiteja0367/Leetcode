class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph={}
        for (a,b), value in zip(equations,values):
            if a not in graph:
                graph[a]=[]
            if b not in graph:
                graph[b]=[]
            graph[a].append((b,value))
            graph[b].append((a, 1 / value))
        def dfs(src,dst,product,visited):
            if src==dst:
                return product
            visited.add(src)
            for neighbor, weight in graph[src]:
                if neighbor not in visited:
                    result=dfs(neighbor,dst,product*weight,visited)
                    if result!=-1:
                        return result
            return -1
        answer=[]
        for src,dst in queries:
            if src not in graph or dst not in graph:
                answer.append(-1.0)
            else:
                visited=set()
                answer.append(dfs(src,dst,1,visited))
        return answer
            
            


        