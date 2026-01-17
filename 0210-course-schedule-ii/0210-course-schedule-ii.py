class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
            taken = []  
            while q:
                curr = q.popleft()
                taken.append(curr) 
                for nei in prereqMap[curr]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
            return taken if len(taken) == numCourses else []   
        return bfs()