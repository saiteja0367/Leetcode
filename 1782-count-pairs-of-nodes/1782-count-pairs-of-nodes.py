class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        # degree = [0] * n
        # edge_count = defaultdict(int)
        # for u, v in edges:
        #     u -= 1
        #     v -= 1
        #     degree[u] += 1
        #     degree[v] += 1
        #     if u < v:
        #         edge_count[(u, v)] += 1
        #     else:
        #         edge_count[(v, u)] += 1
        # answers = []
        # for q in queries:
        #     count = 0   
        #     for i in range(n):
        #         for j in range(i + 1, n):
        #             total = degree[i] + degree[j] 
        #             if i < j:
        #                 direct = edge_count[(i, j)]
        #             else:
        #                 direct = edge_count[(j, i)]
        #             incident = total - direct
        #             if incident > q:
        #                 count += 1
        #     answers.append(count)
        # return answers


        degree = [0] * n
        edge_count = defaultdict(int)
        for u, v in edges:
            u -= 1
            v -= 1
            degree[u] += 1
            degree[v] += 1
            
            if u < v:
                edge_count[(u, v)] += 1
            else:
                edge_count[(v, u)] += 1
        sorted_degree = sorted(degree)
        answers = []
        for q in queries:
            count = 0
            left = 0
            right = n - 1
            while left < right:
                if sorted_degree[left] + sorted_degree[right] > q:
                    count += (right - left)
                    right -= 1
                else:
                    left += 1            
            for (u, v), freq in edge_count.items():
                if degree[u] + degree[v] > q and degree[u] + degree[v] - freq <= q:
                    count -= 1
            
            answers.append(count)
        
        return answers

                    
                    