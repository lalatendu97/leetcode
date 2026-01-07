class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, val in enumerate(nums):
            val2 = target - val
            if val2 in nums:
                j = nums.index(val2)
                if i == j:
                    continue
                return [i, j]
        