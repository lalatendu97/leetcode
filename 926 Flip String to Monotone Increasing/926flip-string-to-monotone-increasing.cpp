class Solution {
public:
    int minFlipsMonoIncr(string s) {
        int o = 0, f = 0;

        for (char c : s){
            if (c == '1'){
                o++;
            } else {
                f = min(f + 1, o);
            }
        }
        return f;
    }
};