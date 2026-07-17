class Solution(object):
    def maxProfit(self, k, prices):

        if not prices or k == 0:
            return 0

        buy = [float('-inf')] * k
        sell = [0] * k

        for price in prices:
            for index in range(k):
                prev_sell = sell[index - 1] if index > 0 else 0
                buy[index] = max(buy[index], prev_sell - price)
                sell[index] = max(sell[index], buy[index] + price)

        return sell[k - 1]