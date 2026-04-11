class Solution {
public:
    int minLengthAfterRemovals(vector<int>& nums) {
        int n = nums.size(), i = 0, p = 0;
        int j = n / 2;

        while (i < n / 2 and j < n){
            if (nums[i] != nums[j]){
                i++;
                j++;
                p++;
            } else {
                j++;
            }
        }
        return n - 2*p;
    }
};