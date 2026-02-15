class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        rows = len(targetGrid)
        cols = len(targetGrid[0])

        colors = set()
        for r in range(rows):
            for c in range(cols):
                colors.add(targetGrid[r][c])

        # Finding the  bounding rectangle
        bounds = {}
        for color in colors:
            min_r, max_r = rows, -1
            min_c, max_c = cols, -1
            
            for r in range(rows):
                for c in range(cols):
                    if targetGrid[r][c] == color:
                        min_r = min(min_r, r)
                        max_r = max(max_r, r)
                        min_c = min(min_c, c)
                        max_c = max(max_c, c)
            
            bounds[color] = (min_r, max_r, min_c, max_c)

        # Building the  dependency graph
        graph = defaultdict(list)
        indegree = {color: 0 for color in colors}

        for color in colors:
            min_r, max_r, min_c, max_c = bounds[color]
            for r in range(min_r, max_r + 1):
                for c in range(min_c, max_c + 1):
                    if targetGrid[r][c] != color:
                        other = targetGrid[r][c]
                        graph[color].append(other)

        # Removing the  duplicates
        for color in graph:
            graph[color] = list(set(graph[color]))

        # Computing  indegree
        for color in graph:
            for nei in graph[color]:
                indegree[nei] += 1

        # Topological sort
        q = deque()
        for color in colors:
            if indegree[color] == 0:
                q.append(color)

        visited = 0

        while q:
            curr = q.popleft()  
            visited += 1
            for nei in graph[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return visited == len(colors)