class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        #in first step we will be computing overall gcd
        overall=nums[0]
        for i in range(1,n):
            overall=gcd(overall,nums[i])
        if overall!=1:
            return -1
        #if there is one already exist
        ones=nums.count(1)
        if ones>0:
            return n-ones
        min_len=n
        #finding the shortest sub array with gcd=1
        for i in range(n):
            current=nums[i]
            for j in range(i+1,n):
                current=gcd(current,nums[j])
                if current==1:
                    min_len=min(min_len,j-i+1)
                    break
        return (min_len-1)+(n-1)
        

