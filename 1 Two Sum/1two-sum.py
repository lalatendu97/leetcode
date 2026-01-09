class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, val in enumerate(nums):
            val2 = target - val
            if val2 in seen:
                return [seen[val2], i]
            seen[val] = i
                