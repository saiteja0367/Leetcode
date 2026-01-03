class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<=nums[-1]:
            return nums[0]
        n=len(nums)
        low=0
        high=n-1
        while low<high:
            mid=(low+high)//2
            if nums[0]<=nums[mid]:
                low=mid+1
            else:
                high=mid
        return nums[low]
            