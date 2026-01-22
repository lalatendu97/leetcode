class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        import numpy as np

        m, n = np.shape(mat)
        mat = np.pad(np.array(mat), pad_width=k)
        res = np.zeros((m, n)).astype(int)

        for i in range(k, m + k):
            for j in range(k, n + k):
                res[i - k, j - k] = np.sum(mat[i - k : i + k + 1, j - k : j + k + 1])
        return res.tolist()