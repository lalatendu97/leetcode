class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        from numpy import square, subtract
        def dist(p1, p2):
            return sum(square(subtract(p2, p1)))
        d = sorted([dist(p1, p2), dist(p2, p3), dist(p3, p4), dist(p4, p1), dist(p1, p3), dist(p4, p2)])
        return True if d.count(d[0]) == 4 and d.count(d[4]) == 2 and d[4] == 2 * d[0] else False