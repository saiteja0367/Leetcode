class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n=len(nums)
        prefix=[0]*(n+1)
        for i in range(n):
            prefix[i+1]=prefix[i]+nums[i]
        q=deque()
        min_len=float('inf')
        for j in range(n+1):
            #we are checking for valid sub array
            while q and prefix[j]-prefix[q[0]]>=k:
                min_len=min(min_len,j-q.popleft())
            #we are maintaining the increasing order
            while q and prefix[j]<=prefix[q[-1]]:
                q.pop()
            q.append(j)
        return min_len if min_len != float('inf') else -1
       

       #t.c->O(n)
       #s.c->0(n)