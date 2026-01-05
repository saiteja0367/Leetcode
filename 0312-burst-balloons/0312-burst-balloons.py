class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #recursion approach
        # nums=[1]+nums+[1]
        # def solve(L,R):
        #     if L>R:
        #         return 0
        #     max_coins=0
        #     for i in range(L,R+1):
        #         coins = (
        #             solve(L, i-1)
        #             + nums[L-1] * nums[i] * nums[R+1]
        #             + solve(i+1, R)
        #         )
        #         max_coins=max(max_coins,coins)
        #     return max_coins
        # return solve(1, len(nums) - 2)

        # #memoziation
        # nums=[1]+nums+[1]
        # n=len(nums)
        # memo=[[-1]*n for _ in range(n)]
        # def solve(L,R):
        #     if L>R:
        #         return 0
        #     if memo[L][R]!=-1:
        #         return memo[L][R]
        #     max_coins=0
        #     for i in range(L,R+1):
        #         coins = (
        #             solve(L, i-1)
        #             + nums[L-1] * nums[i] * nums[R+1]
        #             + solve(i+1, R)
        #         )
        #         max_coins=max(max_coins,coins)
        #         memo[L][R]=max_coins
        #     return max_coins
        # return solve(1,n-2)

        #tabulation
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for length in range(1, n - 1):
            for L in range(1, n - length):
                R = L + length - 1
                for i in range(L, R + 1):
                    dp[L][R] = max(
                        dp[L][R],
                        dp[L][i - 1]
                        + nums[L - 1] * nums[i] * nums[R + 1]
                        + dp[i + 1][R]
                    )
        return dp[1][n - 2]

