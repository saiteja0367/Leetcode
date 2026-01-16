class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # n=len(nums)
        # count=0
        # for i in range(n):
        #     for j in range(i,n):
        #         a=nums[i:j+1]
        #         if sum(a)==k:
        #             count+=1
        # return count
        count=0
        curr_sum=0
        prefix={0:1}
        for num in nums:
            curr_sum+=num
            if curr_sum-k in prefix:
                count+=prefix[curr_sum-k]
            prefix[curr_sum]=prefix.get(curr_sum,0)+1
        return count