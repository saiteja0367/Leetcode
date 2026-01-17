class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)+1
        par=[i for i in range(n)]
        rank=[1]*n
        def find(n1):
            res=n1
            while res!=par[res]:
                par[res]=par[par[res]]
                res=par[res]
            return res
        def union(n1,n2):
            p1=find(n1)
            p2=find(n2)
            if p1==p2:
                return False
            if rank[p2]>rank[p1]:
                par[p1]=p2
                rank[p2]+=rank[p1]
            else:
                par[p2]=p1
                rank[p1]+=rank[p2]
            return True
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]

        

        