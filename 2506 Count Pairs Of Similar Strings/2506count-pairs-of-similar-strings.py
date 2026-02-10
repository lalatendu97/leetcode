class Solution:
    def similarPairs(self, words: List[str]) -> int:
        from math import comb
        res = {}
        count = 0
        for i in words: 
            s = "".join(sorted(set(i)))
            if s in res:
                res[s] += 1
            else:
                res[s] = 1
        return sum([comb(i, 2) for i in res.values()])
        