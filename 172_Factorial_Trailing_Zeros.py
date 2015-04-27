class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        ans = 0
        while n > 0:
            n /= 5
            ans += n
        return ans
