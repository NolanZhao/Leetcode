#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;


class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        if(nums.size() <= 1)
            return false;
        unordered_map<int, bool> m;
        for(int i = 0; i < nums.size(); i++)
        {
            if(m[nums[i]] == true)
                return true;
            m[nums[i]] = true;
        }
        return false;
        
    }
};