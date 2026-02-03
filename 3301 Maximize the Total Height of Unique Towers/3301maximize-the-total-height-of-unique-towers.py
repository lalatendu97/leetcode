class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        
        prev = 10**18  
        total = 0

        for h in maximumHeight:
            assigned = min(h, prev - 1)
            if assigned <= 0:
                return -1
            total += assigned
            prev = assigned

        return total
