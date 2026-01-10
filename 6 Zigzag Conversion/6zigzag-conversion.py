class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        c = 1
        sign = -1
        news = {}

        for i in range(numRows):
            news[i+1] = ""

        for i in s:
            news[c] += i
            
            if c == numRows or c == 1:
                sign *= -1

            c += sign

        return ''.join(news.values())