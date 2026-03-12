class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        int i = 0, c = 1, n = nums.size();
        while(i < n && nums[i] < 1){i++;}

        while(true){
            if (i < n && nums[i] == c){
                while(i < n && nums[i] == c){i++;}
            } else {return c;}
            c++;
        }
        return c;
    }
};