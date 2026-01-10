class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        int_M = 2147483648
        int_m = -2147483648
        rev = 0
        x *= sign
        c = 0

        while x:
            c += 1
            digit = x % 10
            x = x //10
            rev = rev*10 + digit
        
        if c == 10:
            if rev * sign >= int_M:
                return 0 
            elif rev * sign < int_m:
                return 0
        return rev * sign
            