class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        for i in range(1, n):
            nums[i] += nums[i-1]

        if nums[-1] - nums[0] == 0:
            return 0
        
        for i in range(1, n-1):
            if nums[i-1] == nums[-1] - nums[i]:
                return i 
        
        if nums[-2] == 0:
            return n-1
        return -1