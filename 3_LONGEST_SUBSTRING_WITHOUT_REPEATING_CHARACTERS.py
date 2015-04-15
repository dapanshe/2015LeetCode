class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        dic = {}
        i = 0
        ans = 0
        localMax = 0
        while i < len(s):
            if s[i] not in dic:
                localMax += 1
                dic[s[i]] = i
            else:
                localMax = min(localMax+1, i - dic[s[i]])
                dic[s[i]] = i
            ans = max(localMax, ans)
            i += 1
        return ans
