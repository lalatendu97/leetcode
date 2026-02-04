class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        f1 = 0
        f2 = 0
        for i in range(len(arr) - 1):
            s = arr[i+1] - arr[i]
            if f2 == 0: 
                if s > 0:
                    f1 = 1
                    continue
                elif s < 0:
                    f2 = 1
                    continue
                return False
            elif s >= 0:
                return False
        return True if f1 == 1 and f2 == 1 else False
