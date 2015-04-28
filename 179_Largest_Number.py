class Solution:
    # @param {integer[]} nums
    # @return {string}
    # sort by n/(pow(10,len)-1)
    # edge case: all are "0"s
    def largestNumber(self, nums):
        if nums == []:
            return 0
        lis = []
        for i in range(0, len(nums)):
            n = nums[i]
            n_len = len(str(n))
            lis.append([float(n)/(pow(10,n_len)-1), n])
        lis.sort(key = lambda x:-x[0])
        ans = ''
        for [k, n] in lis:
            ans = ans + str(n)
        if len(ans) == ans.count('0'):
            return "0"
        return ans
