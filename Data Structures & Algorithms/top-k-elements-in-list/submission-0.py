class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 0
        d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        res = []
        for key, value in d.items():
            res.append(key)
        return res[:k]