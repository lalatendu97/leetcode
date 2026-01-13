class Solution:
    def myAtoi(self, s: str) -> int:
        res = "0"
        lim = 2147483648
        neg = 1
        dig = False

        for idx, val in enumerate(s):
            if not dig:
                if val == " ":
                    continue

                elif val == "-" or val == "+" and neg == 1:
                    neg = int(val + "1")
                    dig = True
                    continue

            if val.isdigit():
                res += val
                dig = True
                continue

            break

        res = neg * int(res)

        if res < -lim:
            return -lim
        elif res >= lim:
            return lim -1
        else:
            return res

