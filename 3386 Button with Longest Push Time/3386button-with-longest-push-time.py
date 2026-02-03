class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        res = {events[0][0]: events[0][1]}

        for i in range(1, len(events)):
            if events[i][0] in res:
                res[events[i][0]] = max(res[events[i][0]], events[i][1] - events[i-1][1])
            else:
                res[events[i][0]] = events[i][1] - events[i-1][1]

        return max(sorted(res.items(), key=lambda x: x[0]), key=lambda x: x[1])[0]

