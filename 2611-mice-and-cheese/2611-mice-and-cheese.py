class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        total=sum(reward2)
        gains = [r1 - r2 for r1, r2 in zip(reward1, reward2)]
        heap=[]
        for gain in gains:
            heapq.heappush(heap, gain)
            if len(heap) > k:
                heapq.heappop(heap)
        return total + sum(heap)