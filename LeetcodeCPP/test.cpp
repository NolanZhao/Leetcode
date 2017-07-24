class Solution{
public:
    vector<int> plusOne(vector<int> &digits) {
        int carry = 1;
        vector<int> res(digits.size(), 0);
        for (int i = digits.size() - 1; i >= 0; i--) {
            carry += digits[i];
            res[i] = carry % 10;
            carry /= 10;
        }
        if (carry) res.insert(res.begin(), 1);
        return res;
    }
};