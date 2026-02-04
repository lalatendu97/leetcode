class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        p, s = 0, 0

        for i in nums:
            if i > 0:
                p += 1
            elif i < 0:
                s += 1
        return max(p, s)