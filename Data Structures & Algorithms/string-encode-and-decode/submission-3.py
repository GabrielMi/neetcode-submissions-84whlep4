class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            for c in s:
                res += c
            res += '\n'
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            string = ''
            while s[i] != '\n':
                string += s[i]
                i += 1
            res.append(string)
            i += 1
        return res
