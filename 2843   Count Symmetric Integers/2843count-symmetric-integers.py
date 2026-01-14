class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        lst2 = []
        lst4 = []
        res = 0

        for i in range(low, high + 1): 
            if len(str(i)) == 2: 
                lst2.append(i)
            elif len(str(i)) == 4:
                lst4.append(i)

        if lst2:
            for i in lst2:
                if i % 11 == 0:
                    res += 1
        
        if lst4:
            for i in lst4:
                i = str(i)
                if int(i[0]) + int(i[1]) == int(i[2]) + int(i[3]):
                    res += 1

        return res