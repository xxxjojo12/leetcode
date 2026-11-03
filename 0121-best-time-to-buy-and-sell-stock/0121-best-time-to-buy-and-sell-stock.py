class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l = 0
        max_profit = 0

        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r

        return max_profit