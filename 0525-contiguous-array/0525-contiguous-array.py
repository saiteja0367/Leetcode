class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
            diff_index = {0: -1}   # very important
            diff = 0
            res = 0
            for i, n in enumerate(nums):
                if n == 1:
                    diff += 1
                else:
                    diff -= 1
                if diff in diff_index:
                    res = max(res, i - diff_index[diff])
                else:
                    diff_index[diff] = i
            return res

            #t.c->o(n)
            #s.c->o(n)