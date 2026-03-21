class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        import heapq
        res = 0
        heap = []
        i = 0
        n = len(apples)

        while heap or i < n:
            if i < n:
                heapq.heappush(heap, (i + days[i], apples[i]))
            while heap and heap[0][0] <= i:
                heapq.heappop(heap)
            if heap:
                e, c = heapq.heappop(heap)
                if c > 1:
                    c -= 1
                    res += 1
                    if e > i:
                        heapq.heappush(heap, (e, c))
                elif c == 1:
                    res += 1
            i += 1

        return res


