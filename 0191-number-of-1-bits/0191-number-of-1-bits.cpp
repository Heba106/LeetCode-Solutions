class Solution {
public:
    int hammingWeight(uint32_t n) {
        int counter=0;
        for (int i=0; i<32; i++){
            if (n&1){counter++;}
            n>>=1;
        }
        return counter;
    }
};