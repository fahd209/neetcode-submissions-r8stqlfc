class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        i = 0
        j = 1
        max_profit = 0
        cur_profit = 0

        while j < len(prices):
            cur_profit = prices[j] - prices[i]
            if cur_profit < 0:
                i = j
            max_profit = max(max_profit, cur_profit)
            j += 1


        return max_profit 