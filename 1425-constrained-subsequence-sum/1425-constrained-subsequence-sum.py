class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        dp=nums[:]
        dq=deque() #i will store the indices and will maintain the decreasing dp order
        for j in range(n):
            #i will remove the indcies of i where i<j-k because j-i>k will violate the given constraints
            while dq and dq[0]<j-k:
                dq.popleft()
            if dq:
                dp[j]+=max(0,dp[dq[0]]) #which means dp[j] = nums[j] + max(0, best dp in window)
            while dq and dp[dq[-1]]<=dp[j]:
                dq.pop()
            dq.append(j)
        return max(dp)

        #t.c->o(n)
        #s.c->o(n)

