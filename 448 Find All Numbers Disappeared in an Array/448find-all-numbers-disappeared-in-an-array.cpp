class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> res(nums.size());
        vector<int> res2;

        for (int i = 0; i < nums.size(); i++){
            res[nums[i] - 1] = 1;
        }
        for (int i = 0; i < nums.size(); i++){
            if (res[i] == 0){
                res2.push_back(i + 1);
            }
        }
        return res2;

    }
};