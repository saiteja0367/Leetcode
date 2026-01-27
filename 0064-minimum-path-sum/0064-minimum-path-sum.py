class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # m=len(grid)
        # n=len(grid[0])
        # INF=float('inf')
        # dp = [[INF] * (n + 1) for _ in range(m + 1)]
        # dp[1][1]=grid[0][0]
        # for i in range(1,m+1):
        #     for j in range(1,n+1):
        #         if i==1 and j==1:
        #             continue
        #         dp[i][j]=grid[i-1][j-1]+min(dp[i-1][j],dp[i][j-1])
        # return dp[m][n]
        m = len(grid)
        n = len(grid[0])

        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(m):
            for j in range(n):
                if j == 0:
                    dp[j] = dp[j] + grid[i][j]   # only from top
                else:
                    dp[j] = min(dp[j], dp[j-1]) + grid[i][j]

        return dp[n-1]
                
                