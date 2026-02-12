class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        from math import gcd
        res, n = 0, len(nums)

        d = [[int(str(i)[0]), i % 10] for i in nums]
        for i in range(n):
            for j in range(i+1, n):
                if gcd(d[i][0], d[j][1]) == 1:
                    res += 1
        return res

        