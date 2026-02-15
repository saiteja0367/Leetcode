class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        prereqMap = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        for i, j in prerequisites:
            prereqMap[i].append(j)
            indegree[j] += 1
        def bfs():
            q = deque()
            ind = indegree[:]
            for i in range(numCourses):
                if ind[i] == 0:
                    q.append(i)
            preSet = [set() for _ in range(numCourses)]
            while q:
                curr = q.popleft()
                for nei in prereqMap[curr]:
                    preSet[nei].add(curr)
                    preSet[nei].update(preSet[curr])
                    ind[nei] -= 1
                    if ind[nei] == 0:
                        q.append(nei)
            result=[]
            for u,v in queries:
                if u in preSet[v]:
                    result.append(True)
                else:
                    result.append(False)
            return result
        return bfs()

        