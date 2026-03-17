class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        res = 0
        i = 0

        while total - i * cost1 > 0:
            res += (total - i * cost1) // cost2 + 1
            i += 1

        return res + 1 if total - i * cost1 == 0 else res