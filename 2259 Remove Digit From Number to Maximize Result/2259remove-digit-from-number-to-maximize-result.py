class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n = len(number) - 1
        idx = [i for i, val in enumerate(number) if val == digit]
        for i in idx:
            if i < n and int(number[i + 1]) > int(number[i]):
                return number[ : i] + number[i + 1 : ]
        return number[ : idx[-1]] + number[idx[-1] + 1 : ]
            