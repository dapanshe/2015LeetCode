class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dic = {}
        ans = []
        index = 0
        while index < len(num):
            expectValue = target - num[index]
            if expectValue in dic:
                ans.append(dic[expectValue]+1)
                ans.append(index+1)
                break
            else:
                dic[num[index]] = index
            index += 1
        return ans
