class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0] * len(nums) 
        product = 1
        hasZero = False
        for n in nums:
            if n != 0:
                product *= n
            else:
                hasZero = True
        res = []
        if hasZero:
            for i in range(len(nums)):
                if nums[i] != 0:
                    res.append(0)
                else:
                    res.append(product)
        else:
            for i in range(len(nums)):
                res.append(product//nums[i])
        return res