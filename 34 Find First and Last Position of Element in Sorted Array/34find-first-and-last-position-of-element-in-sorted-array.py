class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if target not in nums:
            return [-1, -1]
        i = nums.index(target)
        j = i

        while j < n and nums[j] == target:
            j += 1

        return [i, j - 1]


        # if n == 0:
        #     return [-1, -1]
        # idx = (n - 1) // 2

        # while idx > 0 and idx != n - 1 and nums[idx] != target:
            
        #     if nums[idx] > target:
        #         n = idx
        #         idx = idx // 2

        #     elif nums[idx] < target:
        #         idx = (idx + n) // 2
        
        # i, j = idx, idx

        # print (idx)
        # if nums[i] != target and nums[j] != target:
        #     return [-1, -1]

        # while i >= 0 and nums[i] == target:
        #     i -= 1
        # while j < n and nums[j] == target:
        #     j += 1

        # return [i + 1, j - 1]
        
