class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy = prices[0]
        profit = 0

        for i in range(len(prices)):
            best_buy = min(best_buy, prices[i])
            cur = prices[i]- best_buy
            profit = max(profit, cur)

        return profit
        