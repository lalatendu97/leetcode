class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        res = 0

        for i in s:
            if count < 0:
                res += 1
                count = 0

            if i == '(':
                count += 1
            elif i == ')':
                count -= 1
        if count < 0:
            res += 1
            count = 0
        
        return res + count