class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for idx, val in enumerate(nums):
            if idx > 0 and val == nums[idx - 1]:
                continue
                
            if val > 0:
                break

            l, r = idx + 1, n - 1
            while l < r:
                test = val + nums[l] + nums[r]
                if test < 0:
                    l += 1
                elif test > 0:
                    r -=1
                else:
                    # if [val, nums[l], nums[r]] not in res:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        
        return res
