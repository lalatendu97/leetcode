class Solution:
    def scoreOfString(self, s: str) -> int:
        res = [ord(i) for i in s]

        s = 0
        for i in range(len(res) - 1):
            s += abs(res[i] - res[i + 1])
        return s