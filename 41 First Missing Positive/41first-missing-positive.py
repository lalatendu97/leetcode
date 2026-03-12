class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i = 0

        while i < n and nums[i] < 1:
            i += 1

        c = 1
        while True:
            if i < n and nums[i] == c:
                while i < n and nums[i] == c:
                    i +=1
            else:
                return c
            c += 1
        return c