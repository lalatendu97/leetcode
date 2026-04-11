class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n, i = len(nums), 0
        j = (n + 1) // 2
        p = 0

        
        while i < n // 2 and j < n:
            if nums[i] != nums[j]:
                i += 1
                j += 1
                p += 1
            else:
                j += 1
            
        return n - 2*p