class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        if hamsters == "H" or "HHH" in hamsters or hamsters[:2] == "HH" or hamsters[-2:] == "HH":
            return -1 

        res = 0
        idx = [i for i, val in enumerate(hamsters) if val == "H"]
        
        n = len(idx)
        if n < 2:
            return n

        idx = [idx[i + 1] - idx[i] for i in range(len(idx) - 1)] + [idx[-1]]
        
        i = 0
        while i < n:
            i += 2 if idx[i] == 2 else 1            
            res += 1
        return res