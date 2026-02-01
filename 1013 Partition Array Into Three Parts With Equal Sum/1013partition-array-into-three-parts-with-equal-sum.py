class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s = sum(arr)
        if s % 3 != 0:
            return False
        
        s = s / 3
        n = len(arr)
        for i in range(1, n):
            arr[i] += arr[i-1]

        if s not in arr:
            return False

        i = arr.index(s)
        for x in range(i+1, n-1):
            if arr[x] - arr[i] == s and arr[n-1] - arr[x] == s:
                return True
        return False
