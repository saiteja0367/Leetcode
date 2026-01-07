class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flat_list = [item for row in matrix for item in row]
        flat_list.sort()
        return flat_list[k-1]