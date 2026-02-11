class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k==0:
            return 0 if nums1 == nums2 else -1
        dec=0
        inc=0
        for a,b in zip(nums1,nums2):
            diff=b-a
            if diff%k!=0:
                return -1
            if diff>0:
                inc+=diff//k
            elif diff<0:
                dec+=(-diff)//k
        return inc if inc==dec else -1