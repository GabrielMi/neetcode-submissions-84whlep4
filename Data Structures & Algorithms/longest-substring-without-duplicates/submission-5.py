class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length, l, r, hashSet = 1, 0, 0, set()
        while r < len(s):
            if s[r] in hashSet:
                while s[l] != s[r]:
                    hashSet.remove(s[l])
                    l += 1
                hashSet.remove(s[l])
                l += 1
            else:
                hashSet.add(s[r])
                r += 1
            length = max(length, len(hashSet))
        return length if s else 0
        