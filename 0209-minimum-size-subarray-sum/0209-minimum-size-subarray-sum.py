class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # n=len(nums)
        # min_len=float('inf')
        # for i in range(n):
        #     current_sum=0
        #     for j in range(i,n):
        #         current_sum+=nums[j]
        #         if current_sum>=target:
        #             min_len=min(min_len,j-i+1)
        #             break
        # return 0 if min_len==float('inf') else min_len

        n=len(nums)
        min_len=float('inf')
        left=0
        current_sum=0
        for right in range(n):
            current_sum+=nums[right]
            while current_sum>=target:
                min_len=min(min_len,right-left+1)
                current_sum-=nums[left]
                left+=1
        return 0 if min_len==float('inf') else min_len
