class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set()
        for n in nums:
            hashSet.add(n)
        lengths = []
        for n in nums:
            l = 1
            if n - 1 not in hashSet:
                for i in range(1, len(nums)):
                    if n + i in hashSet:
                        l += 1
                    else:
                        break
            lengths.append(l)
        return max(lengths) if lengths else 0
