class Solution {
public:
    int missingMultiple(vector<int>& nums, int k) {
        int n = 100 / k;
        vector<int> res(n);
        fill(res.begin(), res.end(), 1);

        for (int i: nums){
            if (i % k == 0){
                res[(int) i / k - 1] = 0;
            }
        }
        auto idx = find(res.begin(), res.end(), 1);
        if (idx != res.end()){
            int f = idx - res.begin();
            return (f + 1)*k;
        } else {
            return k*(n+1);
        }
    }
};