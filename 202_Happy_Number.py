class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        dic = {}
        if n == 1:
            return True
        dic[n] = ""
        while True:
            res = self.calc(n)
            if res == 1:
                return True
            if res in dic:
                return False
            else:
                dic[res] = ""
                n = res

    def calc(self, n):
        ans = 0
        while n >= 10:
            ans += (n%10) * (n%10)
            n = n/10
        ans += n*n
        return ans
