class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        v = "aeiou"
        n = len(words)
        count = [0] * (n+1)

        for i, val in enumerate(words):
            count[i+1] = count[i] + (1 if val[0] in v and val[-1] in v else 0)
  
        ans = []
        for l, r in queries:
            ans.append(count[r + 1] - count[l])
        return ans