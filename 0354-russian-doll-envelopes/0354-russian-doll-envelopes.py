class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        heights = [h for _, h in envelopes]
        res = []
        for h in heights:
            if not res or h > res[-1]:
                res.append(h)
            else:
                low, high = 0, len(res) - 1
                while low < high:
                    mid = (low + high) // 2
                    if res[mid] < h:
                        low = mid + 1
                    else:
                        high = mid
                res[low] = h

        return len(res)
