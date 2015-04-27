class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        ans = 0
        length = len(prices)
        x = [0 for i in range(0, length)]
        y = [0 for i in range(0, length)]
        cur_min = prices[0]
        local_max = 0
        for i in range(0, length):
            local_max = max(local_max, prices[i] - cur_min)
            cur_min = min(cur_min, prices[i])
            x[i] = local_max
        cur_max = prices[-1]
        local_max = 0
        for i in range(length - 1, -1, -1):
            local_max = max(local_max, cur_max - prices[i])
            cur_max = max(cur_max, prices[i])
            y[i] = local_max
            ans = max(ans, x[i] + y[i])
        return ans
