#include <iostream>
#include <vector>
using namespace std;

class Solution
{
  public:
    int rob(vector<int> &num)
    {
        if (num.empty())
        {
            return 0;
        }
        int size = num.size();
        vector<int> dp(size, 0);

        dp[0] = num[0];
        dp[1] = max(num[0], num[1]);
        for (int i = 2; i < size; i++)
        {
            dp[i] = max(dp[i - 1], dp[i - 2] + num[i]);
        }
        return dp[size - 1];
    }
};

int main()
{
    Solution solution;
    vector<int> num = {4, 2, 1, 3, 2};
    cout << solution.rob(num) << endl;
    return 0;
}
