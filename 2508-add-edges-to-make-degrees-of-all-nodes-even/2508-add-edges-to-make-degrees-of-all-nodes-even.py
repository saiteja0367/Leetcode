class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        degree=[0]*(n+1)
        connections=set()
        for u,v in edges:
            degree[u]+=1
            degree[v]+=1
            if u < v:
                connections.add((u, v))
            else:
                connections.add((v,u))
        odd = [i for i in range(1, n + 1) if degree[i] % 2]
        if len(odd) == 0:
            return True
        if len(odd) == 2:
            a, b = odd
            if (min(a, b), max(a, b)) not in connections:
                return True
            return any(
                (min(a, i), max(a, i)) not in connections and
                (min(b, i), max(b, i)) not in connections
                for i in range(1, n + 1) if i != a and i != b
            )
        if len(odd) == 4:
            a, b, c, d = odd
            return (
                ((min(a,b),max(a,b)) not in connections and
                 (min(c,d),max(c,d)) not in connections) or
                ((min(a,c),max(a,c)) not in connections and
                 (min(b,d),max(b,d)) not in connections) or
                ((min(a,d),max(a,d)) not in connections and
                 (min(b,c),max(b,c)) not in connections)
            )
        return False