class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            prev=res[-1]
            curr=intervals[i]
            if prev[1]>=curr[0]:
                prev[1]=max(prev[1],curr[1])
            else:
                res.append(curr)
        return res

        # intervals.sort()
        # ans=[]
        # n=len(intervals)
        # i=0
        # while i<n:
        #     start=intervals[i][0]
        #     end=intervals[i][1]
        #     j=i+1
        #     while j<n and intervals[j][0]<=end:
        #         end=max(end,intervals[j][1])
        #         j+=1
        #     ans.append([start,end])
        #     i=j
        # return ans
