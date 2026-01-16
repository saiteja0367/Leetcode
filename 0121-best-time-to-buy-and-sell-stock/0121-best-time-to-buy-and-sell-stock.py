class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # n=len(prices)
        # max_profit=0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if prices[i]<prices[j]:
        #             profit=prices[j]-prices[i]
        #             max_profit=max(profit,max_profit)
        # return max_profit
        n=len(prices)
        min_price=float('inf')
        max_profit=0
        for i in range(n):
            if prices[i]<min_price:
                min_price=prices[i]
            profit=prices[i]-min_price
            if profit>max_profit:
                max_profit=profit
        return max_profit

        