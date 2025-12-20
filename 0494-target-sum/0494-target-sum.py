class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        total_sum=sum(nums)
        if (total_sum+target)%2!=0 or abs(target)>total_sum:
            return 0
        new_target=(total_sum+target)//2
        dp = [[0] * (new_target + 1) for _ in range(n + 1)]
        dp[0][0]=1
        for i in range(1,n+1):
            num=nums[i-1]
            for s in range(new_target+1):
                dp[i][s]=dp[i-1][s]
                if s>=num:
                    dp[i][s]+=dp[i-1][s-num]
        return dp[n][new_target]


        