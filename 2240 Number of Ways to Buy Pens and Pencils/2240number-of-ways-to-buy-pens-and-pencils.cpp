class Solution {
public:
    long long waysToBuyPensPencils(int total, int cost1, int cost2) {
        int i = 0;
        long long res = 0;

        while(total - i * cost1 > 0){
            res += long((total - i * cost1) / cost2) + 1;
            i++;
        }
        if (total - i * cost1 == 0){res++;}

        return res;
    }
};