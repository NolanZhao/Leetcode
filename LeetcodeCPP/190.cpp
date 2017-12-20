#include <iostream>
using namespace std;


class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t value = 0;
        for (uint32_t i = 0; i < 32; ++i) {
            value = (value<<1 )|((n>>i) & 1);
        }  
        return value;

    }
};