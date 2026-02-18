class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []

        i, j, n1, n2 = 0, 0, len(firstList), len(secondList)
        while i < n1 and j < n2:
            l, u = max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])

            if u == firstList[i][1]:
                i += 1
            if u == secondList[j][1]:
                j += 1

            if l <= u:
                res.append([l, u])
        return res