class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        for i, j in prerequisites:
            prereqMap[j].append(i)
            indegree[i] += 1
        def bfs():
            q = deque()
            for i in range(numCourses):
                if indegree[i] == 0:
                    q.append(i)
            taken = 0
            while q:
                curr = q.popleft()
                taken += 1
                for nei in prereqMap[curr]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
            return taken == numCourses
        return bfs()
