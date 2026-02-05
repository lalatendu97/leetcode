class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))

        res, mxdf = 0, 0
        for atk, df in properties:
            if df < mxdf:
                res += 1
            else:
                mxdf = df  
        return res
        