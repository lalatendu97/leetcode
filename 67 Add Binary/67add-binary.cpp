class Solution {
public:
    string addBinary(string a, string b) {
        int x = stoi(a, nullptr, 2), y = stoi(b, nullptr, 2);
        int t = x + y;
        if (t == 0){return "0";}
        string res = bitset<16>(t).to_string();
        res.erase(0, res.find('1'));
        return res;
    }
};