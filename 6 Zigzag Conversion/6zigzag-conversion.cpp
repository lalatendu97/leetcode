class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1){return s;}
        string a, b, c, res;
        map<int, string> dict;

        for (int idx = 0; idx < numRows; idx++){dict[idx] = "";}

        int i = 0, m = 1;

        for (int idx = 0; idx < s.size(); idx++){
            if (i < 0){
                m = 1;
                i = 1;
            } else if (i == numRows){
                m = -1;
                i = numRows - 2;
            }
            dict[i] += s[idx];
            i += m;
        }

        for (int idx = 0; idx < numRows; idx++){
            res += dict[idx];
        }
        return res;

    }
};