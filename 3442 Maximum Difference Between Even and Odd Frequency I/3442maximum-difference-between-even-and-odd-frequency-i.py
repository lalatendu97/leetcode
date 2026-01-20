class Solution:
    def maxDifference(self, s: str) -> int:
        count = {}
        for i in range(97, 123):
            count[chr(i)] = 0

        for i in s:
            count[i] += 1

        count = sorted(list(set([val for val in count.values()])), reverse=True)[:-1]
        print(count)

        o, e = -1, -1
        for i in range(len(count)):
            if o == -1 and count[i] % 2 == 1:
                o = count[i]
            if e == -1 and count[- i - 1] % 2 == 0:
                e = count[- i - 1]
        return o - e
