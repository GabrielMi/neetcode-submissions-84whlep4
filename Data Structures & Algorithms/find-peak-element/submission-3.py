class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if mid == 0:
                return 0 if nums[0] > nums[1] else 1
            if mid == len(nums) - 1:
                return len(nums) - 1 if nums[-1] > nums[-2] else len(nums) - 2
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid - 1] > nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1
        