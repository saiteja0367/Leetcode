class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        #recursion
        n=len(prices)
        # def dfs(i,buy,cap):
        #     if i==n or cap==0:
        #         return 0
        #     if buy:
        #         return max(
        #             -prices[i] + dfs(i+1, 0, cap),
        #             dfs(i+1, 1, cap)
        #         )
        #     else:
        #         return max(
        #             prices[i] + dfs(i+1, 1, cap-1),
        #             dfs(i+1, 0, cap)
        #         )
        # return dfs(0,1,2)


        #iterative
        n=len(prices)
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                for cap in range(1,3):
                    if buy==0:
                        dp[ind][buy][cap] = max(
                            0 + dp[ind + 1][0][cap],
                            -prices[ind] + dp[ind + 1][1][cap]
                        )
                    else:
                        dp[ind][buy][cap] = max(
                            0 + dp[ind + 1][1][cap],
                            prices[ind] + dp[ind + 1][0][cap - 1]
                        )
        return dp[0][0][2]

