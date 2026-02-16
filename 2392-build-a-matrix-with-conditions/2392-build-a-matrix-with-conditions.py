class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo(graph, indegree):
            q = deque()
            order = []
            for i in range(1, k + 1):
                if indegree[i] == 0:
                    q.append(i)
            while q:
                curr = q.popleft()
                order.append(curr)
                for nei in graph[curr]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
            
            # if any cycle exists we will return []
            if len(order) != k:
                return []      
            return order
        #we will Build the Row Graph
        rowGraph = defaultdict(list)
        rowIndegree = [0] * (k + 1)
        for a, b in rowConditions:
            rowGraph[a].append(b)
            rowIndegree[b] += 1
        
        # we will Build the Column Graph
        colGraph = defaultdict(list)
        colIndegree = [0] * (k + 1)
        
        for a, b in colConditions:
            colGraph[a].append(b)
            colIndegree[b] += 1
        
        # we will Get the Topological Orders
        rowOrder = topo(rowGraph, rowIndegree[:])
        if not rowOrder:
            return []
        
        colOrder = topo(colGraph, colIndegree[:])
        if not colOrder:
            return []
        
        #we will Build the Position Maps
        rowPos = {}
        colPos = {}
        
        for i in range(k):
            rowPos[rowOrder[i]] = i
            colPos[colOrder[i]] = i
        
        #we will Build the Matrix
        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            r = rowPos[num]
            c = colPos[num]
            matrix[r][c] = num
        return matrix

        #t.c->o(k+m)
        #s.c->o(k+m)
        
        

        