class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            if not strs[i]:
                prefix = ''
            for j in range(min(len(prefix), len(strs[i]))):
                if prefix[j] != strs[i][j]:
                    prefix = prefix[:j]
                    break
                if len(prefix) > len(strs[i]) and j == len(strs[i]) - 1:
                    prefix = strs[i]
        return prefix
        