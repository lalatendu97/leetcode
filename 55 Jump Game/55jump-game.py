class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        n -= 1

        f = 0
        idx = 0
        while idx <= f:
            f = max(f, idx + nums[idx])
            if f >= n:
                return True
            idx += 1
        return False