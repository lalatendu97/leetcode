class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 1
        n = len(strs[0])
        while i <= n:
            res = {}
            for word in strs:
                res[word[:i]] = 1

            if len(res) == 1:
                i += 1
                continue
            break
        return strs[0][:i-1]