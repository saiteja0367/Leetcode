class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # n=len(s)
        # max_len=0
        # for i in range(n):
        #     seen=set()
        #     for j in range(i,n):
        #         if s[j] in seen:
        #             break
        #         seen.add(s[j])
        #         max_len=max(max_len,j-i+1)
        # return max_len
        n=len(s)
        l=0
        seen=set()
        max_len=0
        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            max_len=max(max_len,r-l+1)
        return max_len
