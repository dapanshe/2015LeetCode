class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bin_str = bin(n)
        head = bin_str[:2]
        tail = bin_str[2:]
        tail = '0' * (32 - len(tail)) + tail
        ans_str = head + tail[::-1]
        return int(ans_str,2)
