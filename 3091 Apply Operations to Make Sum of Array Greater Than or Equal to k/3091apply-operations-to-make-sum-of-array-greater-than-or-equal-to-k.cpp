class Solution {
public:
    int minOperations(int k) {
        if (k == 1){return 0;}
        int res = INT_MAX, ops;

        for (int i = 1; i <= k; i ++){
            ops = (k + i - 1) / i + i - 2;
            res = min(ops, res);
        }
        return res;
    }
};