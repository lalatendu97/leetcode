class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = -int(str(-x)[::-1])
            return x if x >= -2**31 else 0
        else:
            x = int(str(x)[::-1])
            return x if x < 2**31 else 0