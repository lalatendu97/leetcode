class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = abs(nums[0])
        ret = nums[0]

        for i in nums:
            if abs(i) <= res:
                res = abs(i)
                ret = i
        return ret