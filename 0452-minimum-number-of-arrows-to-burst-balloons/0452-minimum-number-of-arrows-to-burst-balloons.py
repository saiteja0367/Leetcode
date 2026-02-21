class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        res=len(points)
        prev_end=points[0][1]
        for i in range(1,len(points)):
            curr_start=points[i][0]
            if curr_start<=prev_end:
                res-=1
            else:
                prev_end=points[i][1]
        return res

        #t.c->O(n log n)
        #s.c->O(1)
            
       