class Solution:
    def maximumSwap(self, num: int) -> int:
        lst = list(map(int, str(num)))

        i = 0
        n = len(lst)
        while i < n:
            if lst[i] == max(lst[i:]):
                i += 1
                continue
            break
        
        if i == n:
            return num
        mx = max(lst[i:])
        j = [idx for idx, val in enumerate(lst) if val == mx][-1]
        lst[i], lst[j] = lst[j], lst[i]
        return int(''.join(map(str, lst)))