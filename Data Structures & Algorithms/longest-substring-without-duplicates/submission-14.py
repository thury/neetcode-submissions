class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp = ""
        maxLen = 0
        for i, c in enumerate(s):
            if c in tmp:
                tmp = tmp[tmp.index(c)+1:]
            tmp += c
            if maxLen < len(tmp):
                maxLen = len(tmp)            
        return maxLen