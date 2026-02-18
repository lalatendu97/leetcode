class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        towers = sorted(towers, key=lambda x: x[0])
        score = -1
        res = None

        for i in towers:
            if abs(i[0] - center[0]) + abs(i[1] - center[1]) <= radius: 
                if i[2] > score or i[2] == score and i[0] == res[0] and i[1] < res[1]:
                    score = i[2]
                    res = i[:2]

        return res if res else [-1, -1]