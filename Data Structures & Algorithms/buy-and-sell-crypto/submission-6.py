class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        smallest = prices[0]
        for price in prices:
            if price < smallest:
                smallest = price
            else:
                profit = price - smallest
                if profit > max_profit:
                    max_profit = profit
            
        return max_profit

