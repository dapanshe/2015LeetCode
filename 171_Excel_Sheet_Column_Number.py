class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        lis = list(s)
        ans = 0
        for i in range(0, len(lis)):
            ans = 26*ans + ord(lis[i]) - ord('A') + 1
        return ans
