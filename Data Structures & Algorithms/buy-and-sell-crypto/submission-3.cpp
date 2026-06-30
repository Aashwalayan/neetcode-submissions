#include <algorithm>

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int lowest = prices[0];
        int res = 0;

        for(int i = 0; i < prices.size(); i++){
            lowest = min(lowest, prices[i]);

            res = max(res, prices[i] - lowest);
        }
        return res;        
    }
};
