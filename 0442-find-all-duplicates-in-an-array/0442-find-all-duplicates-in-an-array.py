class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # freq={}
        # duplicates=[]
        # n=len(nums)
        # for num in nums:
        #     freq[num]=freq.get(num,0)+1
        # for num,value in freq.items():
        #     if value>1:
        #         duplicates.append(num)
        # return duplicates

        res=[]
        for n in nums:
            n=abs(n)
            if nums[n-1]<0:
                res.append(n)
            nums[n-1]=-nums[n-1]
        return res


