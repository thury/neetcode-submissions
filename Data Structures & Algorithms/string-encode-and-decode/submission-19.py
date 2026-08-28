class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs:
            s += str(len(string)) + "#" + string
        return s

    def decode(self, s: str) -> List[str]:
        mult = 0
        res = []
        i = 0
        while i < len(s):
            char = s[i]
            if char.isnumeric():
                mult = mult * 10 + int(char)
                i = i + 1
                continue
            if char == '#':
                res.append(str(s[i+1:i+mult+1]))
                i = i + mult + 1
                mult = 0
                continue
        return res