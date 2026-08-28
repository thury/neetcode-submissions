class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minValue = float('inf')
        profit = 0
        for sell in prices:
            if minValue > sell:
                minValue = sell
            if profit < sell - minValue:
                profit = sell - minValue
        if profit < 0:
            return 0
        return profit
