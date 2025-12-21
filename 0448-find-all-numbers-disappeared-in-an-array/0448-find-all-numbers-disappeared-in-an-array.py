class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        unique_elements=set(nums)
        n=len(nums)
        a=[]
        for i in range(1,n+1):
            if i not in unique_elements:
                a.append(i)
        return a 