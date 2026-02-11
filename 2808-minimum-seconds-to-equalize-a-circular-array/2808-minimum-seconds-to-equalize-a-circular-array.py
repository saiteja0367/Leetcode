class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n=len(nums)
        positions=defaultdict(list)
        for i,val in enumerate(nums):
            positions[val].append(i)
        ans=float('inf')
        for pos in positions.values():
            max_gap=0
            #for normal gaps its like adjacent to each other
            for i in range(1, len(pos)):
                max_gap=max(max_gap,pos[i]-pos[i-1])
            #for circular gap
            circular_gap=pos[0] + n - pos[-1]
            max_gap=max(max_gap,circular_gap)
            ans=min(ans,max_gap//2)
        return ans
