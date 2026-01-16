class Solution:
    def maxArea(self, height: List[int]) -> int:
        # n=len(height)
        # max_area=0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         width=j-i
        #         area=min((height[i],height[j]))*width
        #         max_area=max(max_area,area)
        # return max_area
        n=len(height)
        l=0
        r=n-1
        max_area=0
        while l<r:
            width=r-l
            area=min((height[l],height[r]))*width
            max_area=max(max_area,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_area
    
