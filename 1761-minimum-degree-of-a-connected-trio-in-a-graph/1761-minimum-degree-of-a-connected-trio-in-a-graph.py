class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        degree=[0]*n
        connections=set()
        for u,v in edges:
            u-=1
            v-=1
            degree[u]+=1
            degree[v]+=1
            connections.add((u,v))
            connections.add((v,u))
        min_degree = float('inf')
        for i in range(n):
            for j in range(i+1,n):
                if (i,j) in connections:
                    for k in range(j+1,n):
                        if (i,k) in connections and (j,k) in connections:
                            trio_degree=degree[i]+degree[j]+degree[k]-6
                            min_degree=min(min_degree,trio_degree)
        return min_degree if min_degree != float('inf') else -1



        