class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        res = -k-1

        for i, val in enumerate(nums):
            if val == 1:
                if i - res <= k:
                    return False
                res = i
        return True
