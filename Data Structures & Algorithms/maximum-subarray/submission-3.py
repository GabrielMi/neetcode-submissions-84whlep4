class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r, res = 0, 1, nums[0]
        while r < len(nums):
            if sum(nums[l:r]) < 0:
                l = r
            elif nums[r] < -sum(nums[l:r]):
                l = r + 1
                r = l
            res = max(res, sum(nums[l:r + 1]))
            r += 1
        return res
