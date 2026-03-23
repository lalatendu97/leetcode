class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int i = 0, j = nums.size() - 1;
        int m;
        
        while (i <= j){
            m = (i + j) / 2;

            if (nums[m] == target){
                return m;
            } else if (nums[m] < target){
                i = m + 1;
            } else if (nums[m] > target){
                j = m - 1;
            }
        }
        
        return i;
    }
};