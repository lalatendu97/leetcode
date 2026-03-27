class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> res(m + n);
        int i = 0, j = 0, c = 0;

        while(i < m && j < n){
            if (nums1[i] < nums2[j]){
                res[c] = nums1[i];
                i++;
            } else {
                res[c] = nums2[j];
                j++;
            }
            c++;
        }
        while (j < n){
            res[c] = nums2[j];
            j++;
            c++;
        }
        while (i < m){
            res[c] = nums1[i];
            i++;
            c++;
        }

        nums1 = res;
        return;
    }
};