class Solution {
public:
    int possibleStringCount(string word) {
        int i = 0, count, res = 0;

        while (i < word.size()){
            count = 1;
            while (i < word.size() - 1 && word[i] == word[i + 1]){
                count++;
                i++;
            }
            res += count - 1;
            i++;
        }

        return res + 1;
    }
};