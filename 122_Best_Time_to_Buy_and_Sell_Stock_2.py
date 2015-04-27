class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        ans = 0
        has_buy = False
        for i in range(0, len(prices)-1):
            if prices[i] < prices[i+1]:
                if has_buy == False:
                    buy_price = prices[i]
                    has_buy = True
            else:
                if has_buy == True:
                    ans += prices[i] - buy_price
                    has_buy = False
        if has_buy:
            ans += prices[len(prices)-1] - buy_price
        return ans
