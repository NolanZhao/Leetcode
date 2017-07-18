#include <iostream>
#include <vector>
using namespace std;



class Solution {
public:
    int maxSubArray(vector<int> nums) {
        int sum = 0, minSum = 0, maxSum = INT_MIN;
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            maxSum = max(maxSum, sum - minSum);
            minSum = min(minSum, sum);
        }
        return maxSum;
    }

};


int main()
{
    Solution a = Solution();
    int n[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    vector<int> nums = vector<int>(n, n+9);

    int m = a.maxSubArray(nums);
    cout << m << endl;
}