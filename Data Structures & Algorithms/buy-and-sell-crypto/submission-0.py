class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minBuy = prices[0]
        maxSell = -1
        maxProfit = -1000000000
        for price in prices:
            maxProfit = max(maxProfit, price - minBuy)
            minBuy = min(minBuy, price)
        
        return maxProfit
