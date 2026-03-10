class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        auto i = find(nums.begin(), nums.end(), target);
        vector<int> res = {-1, -1};

        if (i != nums.end()){
            int j = i - nums.begin();
            res[0] = i - nums.begin();
            while(j < nums.size() && nums[j] == target){
                j++;
            }
            res[1] = j - 1;

        }   
        return res;
    }
};