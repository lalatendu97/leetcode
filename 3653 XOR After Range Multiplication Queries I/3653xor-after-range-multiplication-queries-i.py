class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        c = 10**9 + 7
        for query in queries:
            idx = query[0]

            while idx <= query[1]:
                nums[idx] = (nums[idx] * query[3]) % c
                idx += query[2]

        res = 0
        for i in nums:
            res = res ^ i

        return res