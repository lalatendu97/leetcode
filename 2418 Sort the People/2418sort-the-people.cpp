class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        map<int, string, greater<int>> dict;
        vector<string> res;

        for (int i = 0; i < heights.size(); i++){
            dict[heights[i]] = names[i];
        }

        for (const auto& it : dict){
            res.push_back(it.second);
        }

        return res;
    }
};