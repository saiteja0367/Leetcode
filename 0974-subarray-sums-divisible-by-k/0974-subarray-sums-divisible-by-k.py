class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum=0
        res=0
        prefix_count=defaultdict(int)
        prefix_count[0]=1
        for n in nums:
            prefix_sum+=n
            remainder=prefix_sum%k
            if remainder in prefix_count:
                res+=prefix_count[remainder]
            prefix_count[remainder]+=1
        return res

        #t.c->o(n)
        #s.c->o(n)        