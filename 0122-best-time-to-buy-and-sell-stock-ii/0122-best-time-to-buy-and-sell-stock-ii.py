class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        profit = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            val = prices[i] - buy
            if val > 0:
                profit += val
                buy = prices[i]
            else:
                buy = prices[i]
            
        
        return profit



