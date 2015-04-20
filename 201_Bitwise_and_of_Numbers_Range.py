class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):
        if len(bin(m)) != len(bin(n)):
            return 0
        k = 0
        while True:
            if m == n:
                return m * pow(2,k)
            if m == 0:
                return 0
            m = m/2
            n = n/2
            k += 1
