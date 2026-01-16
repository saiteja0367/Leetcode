class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        low=0
        high=n-1
        while low<high:
            curr_sum=numbers[low]+numbers[high]
            if curr_sum==target:
                return [low+1,high+1]
            elif curr_sum<target:
                low+=1
            else:
                high-=1