import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        for i in range(len(s)):
            if s[len(s)-i-1] is not s[i]:
                return False
        return True 