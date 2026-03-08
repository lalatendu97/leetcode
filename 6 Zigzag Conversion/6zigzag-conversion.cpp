class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1 || numRows > s.size()){return s;}
        vector<string> res1(numRows);

        int i = 0, m = 1;
        string res = "";

        for (char c : s){
            res1[i] += c;

            if (i == numRows - 1){m = -1;}
            else if (i == 0){m = 1;}
            i += m;
        }

        for (string str : res1){
            res += str;
        }
        return res;

    }
};