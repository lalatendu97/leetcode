class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        if hamsters == "H":
            return -1 

        res = 0
        idx = [i for i, val in enumerate(hamsters) if val == "H"]
        
        n = len(idx)
        if n < 2:
            return n

        if hamsters[:2] == "HH" or hamsters[-2:] == "HH" or "HHH" in hamsters:
            return -1

        idx = [idx[i + 1] - idx[i] for i in range(len(idx) - 1)] + [idx[-1]]
        
        i = 0
        while i < n:
            if idx[i] > 2:
                res += 1
                i += 1
            
            elif idx[i] == 2:
                res += 1
                i += 2

            else:
                res += 1
                i += 1
         
        return res