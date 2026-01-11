class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lst = list(set(nums))
        n = len(lst)
        nums[:n] = sorted(lst)
        return n