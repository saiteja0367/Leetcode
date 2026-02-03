class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n=len(days)
        dp=[0]*(len(days)+1)
        for i in range(n-1,-1,-1):
            cost1=costs[0]+dp[i+1]
            j=i
            while j<n and days[j]<=days[i]+6:
                j+=1
            cost7=costs[1]+dp[j]
            j=i
            while j<n and days[j]<=days[i]+29:
                j+=1
            cost30=costs[2]+dp[j]
            dp[i]=min(cost1,cost7,cost30)
        return dp[0]
        


        
        