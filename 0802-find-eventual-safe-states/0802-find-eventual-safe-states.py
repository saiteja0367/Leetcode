class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        # build outdegree
        outdegree = [0] * n
        for u in range(n):
            outdegree[u] = len(graph[u])

        # build reversed graph
        rev = [[] for _ in range(n)]
        for u in range(n):
            for v in graph[u]:
                rev[v].append(u)

        res = []

        def bfs():
            q = deque()

            # initialize queue with terminal nodes
            for i in range(n):
                if outdegree[i] == 0:
                    q.append(i)

            while q:
                curr = q.popleft()
                res.append(curr)

                for parent in rev[curr]:
                    outdegree[parent] -= 1
                    if outdegree[parent] == 0:
                        q.append(parent)

        bfs()
        return sorted(res)