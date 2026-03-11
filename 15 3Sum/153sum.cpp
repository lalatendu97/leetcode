class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        int l, r;
        int test;

        sort(nums.begin(), nums.end());

        for (int idx = 0; idx < nums.size(); idx++){
            if (nums[idx] > 0){break;}
            if (idx > 0 && nums[idx] == nums[idx - 1]){continue;}
            
            l = idx + 1;
            r = nums.size() - 1;

            while (l < r){
                test = nums[idx] + nums[l] + nums[r];

                if (test < 0){
                    l++;
                } else if(test > 0){
                    r--;
                } else{
                    res.push_back({nums[idx], nums[l], nums[r]});
                    l++;
                    r--;
                    while (l < r && nums[l] == nums[l - 1]){l++;}
                    while (l < r && nums[r] == nums[r + 1]){r--;}
                }
            }
        }
        return res;
    }
};