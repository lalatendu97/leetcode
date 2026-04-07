class Solution {
public:
    vector<int> sortEvenOdd(vector<int>& nums) {
        vector<int> temp1, temp2;

        for (int i = 0; i < nums.size(); i+=2){
            temp1.push_back(nums[i]);
        }

        for (int i = 1; i < nums.size(); i+=2){
            temp2.push_back(nums[i]);
        }

        sort(temp1.begin(), temp1.end());
        sort(temp2.begin(), temp2.end(), greater<int>());

        for (int i = 0; i < nums.size(); i++) {
            if (i % 2 == 0) {
                nums[i] = temp1[i/2];
            } else {
                nums[i] = temp2[(int) i/2];
            }

        }

        return nums;
    }
};