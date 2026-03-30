class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while high - low > 1:
            mid = (low + high) // 2
            if nums[low] < nums[mid] < nums[high]:
                return nums[low]
            elif nums[mid] < nums[low]:
                high = mid
            else:
                low = mid
        return min(nums[low], nums[high])
