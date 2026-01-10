class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        c = 1
        sign = -1
        news = {}

        for _ in range(numRows):
            news[c] = ""
            c += 1

        c = 1

        for i in s:
            news[c] += i
            
            if c == numRows or c == 1:
                sign *= -1

            c += sign

        res = ""
        for i in news:
            res += news[i]

        return res