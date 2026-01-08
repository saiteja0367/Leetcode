class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        # quad=[]
        # results=set()
        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             for l in range(k+1,n):
        #                 if nums[i]+nums[j]+nums[k]+nums[l]==target:
        #                     quad = tuple(sorted([nums[i], nums[j], nums[k], nums[l]]))
        #                     results.add(quad)
        # return [list(q) for q in results]
        nums.sort()
        res = []
        quad = []

        def helper(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    helper(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return

            # base case: 2-sum
            l, r = start, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        helper(4, 0, target)
        return res
