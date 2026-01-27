class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort()
        tasks = [tasks[i] for i in range(3, 4*len(processorTime), 4)]
        res = 0

        for i,j in zip(processorTime[::-1], tasks):
            res = max(res, i + j)

        return res
        



