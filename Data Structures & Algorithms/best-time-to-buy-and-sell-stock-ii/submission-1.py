class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])

        return profit

        # isHoldingAStock = False
        # maxStockProfit = 0
        # last_purchase = None

        # for i in range(len(prices)):
        #     next_price = 0 if i == len(prices) - 1 else prices[i+1]
        #     if isHoldingAStock:
        #         # check if its a good time to sell
        #         if next_price < prices[i]:
        #             isHoldingAStock = False
        #             profit = prices[i] - prices[last_purchase]
        #             maxStockProfit += profit
        #     else:
        #         if next_price > prices[i]:
        #             last_purchase = i
        #             isHoldingAStock = True


        # return maxStockProfit

        