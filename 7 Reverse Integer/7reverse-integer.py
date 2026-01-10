class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        int_M = 2147483648
        int_m = -2147483648
        rev = 0
        x *= sign
        c = len(str(x))

        while x:
            digit = x % 10
            x = x //10
            rev = rev*10 + digit
        
        rev *= sign
        
        if c == 10:
            if rev + 1 > int_M:
                return 0
            if rev < int_m:
                return 0
        return rev
            