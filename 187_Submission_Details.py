class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        if len(s) < 11:
            return []
        dic = {}
        ans = []
        for i in range(0, len(s)-9):
            subStr = s[i:i+10]
            if subStr in dic:
                if dic[subStr] == 1:
                    ans.append(subStr)
                    dic[subStr] = 2
            else:
                dic[subStr] = 1
        return ans
