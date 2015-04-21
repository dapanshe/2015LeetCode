class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        n_str = bin(n)
        return n_str.count('1')
