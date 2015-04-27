class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if prices == []:
            return 0
        cur_min = prices[0]
        ans = 0
        for i in range(0, len(prices)):
            cur_min = min(cur_min, prices[i])
            ans = max(ans, prices[i] - cur_min)
        return ans
