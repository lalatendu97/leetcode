class Solution {
public:
    int reverse(int x) {
        vector<int> rev;
        int a = 0, m = 1; 

        while (x != 0) {
            rev.push_back(x % 10);
            x /= 10;
        }

        for (int i = 0; i < rev.size(); i++){
            if (a > INT_MAX / 10 || (a == INT_MAX / 10 && rev[i] > 7)){return 0;}
            if (a < INT_MIN / 10 || (a == INT_MIN / 10 && rev[i] < -8)){return 0;}
            a = a * 10 + rev[i];
        }
        return a;
    }
};