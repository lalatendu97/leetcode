class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res |= i

        dp = {0 : 1}
        for i in nums:
            temp = dp.copy()
            for ky in dp.keys():
                nky = i | ky
                temp[nky] = temp.get(nky, 0) + dp[ky]
            dp = temp
        
        return dp[res] 
