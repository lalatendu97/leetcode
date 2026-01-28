class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        aidx = []
        bidx = []
        res = []
        
        i = 0
        while a in s[i:]:
            i = s[i:].index(a) + i
            aidx.append(i)
            i += 1
        
        i = 0
        while b in s[i:]:
            i = s[i:].index(b) + i
            bidx.append(i)
            i += 1

        for i in aidx:
            if any(i - k <= x <= i + k for x in bidx):
                res.append(i)
        
        return res
        
