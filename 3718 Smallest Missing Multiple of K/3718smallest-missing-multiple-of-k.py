class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 1

        for val in nums:
            if i * k == val:
                i += 1
        return i * k