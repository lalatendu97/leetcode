class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        res = 1

        inc = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    inc[i] = max(inc[i], inc[j] + 1)
        
        dec = [1] * n
        for i in reversed(range(n)):
            for j in reversed(range(i, n)):
                if nums[j] < nums[i]:
                    dec[i] = max(dec[i], dec[j] + 1)
        
        for i in range(1, n - 1):
            if inc[i] > 1 and dec[i] > 1:
                res = max(res, inc[i] + dec[i] - 1)

        return n - res