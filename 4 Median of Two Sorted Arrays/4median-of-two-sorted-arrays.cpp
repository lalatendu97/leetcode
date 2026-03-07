class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size(), n2 = nums2.size(), i = 0, j = 0;
        int k = n1 + n2, curr = 0, prev = 0;

        for (int z = 0; z <= k / 2; z++){
            prev = curr;
            if (i < n1 && (j >= n2 || nums2[j] > nums1[i])){
                curr = nums1[i];
                i++;
            }
            else {
                curr = nums2[j];
                j++;
            }
        }

        if (k % 2 == 0) {
            return (curr + prev) / 2.0;
        }
        else {
            return curr;
        }
    }
};