class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # n=len(matrix)
        # for i in range(len(matrix)):
        #    for j in range(len(matrix[0])):
        #         if matrix[i][j]==target:
        #             return True
        # return False
        rows=len(matrix)
        cols=len(matrix[0])
        low=0
        high=(rows*cols)-1
        while low<=high:
            mid=(low+high)//2
            row=mid//cols
            col=mid%cols
            mid_ele=matrix[row][col]
            if mid_ele==target:
                return True
            if mid_ele>target:
                high=mid-1
            else:
                low=mid+1
        return False


