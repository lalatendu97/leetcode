class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        from math import comb
        count = sum([1 for i in s if i == c])
        return comb(count, 1) + comb(count, 2)
