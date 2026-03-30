class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = set()
        for n in nums:
            res.add(n)
        return True if len(res) != len(nums) else False