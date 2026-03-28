class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        from collections import defaultdict

        count = defaultdict(int)
        lsum = defaultdict(int)
        res = []

        for i, val in enumerate(arr):
            res.append(count[val]*i - lsum[val])
            count[val] += 1
            lsum[val] += i

        count.clear()
        lsum.clear()

        for i in range(len(arr) - 1, -1, -1):
            res[i] += lsum[arr[i]] - count[arr[i]]*i
            count[arr[i]] += 1
            lsum[arr[i]] += i
        return res