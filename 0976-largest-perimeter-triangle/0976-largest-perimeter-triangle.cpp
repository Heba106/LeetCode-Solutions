class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        sort(nums.begin(), nums.end(), greater<int>());
        while (nums.size()>=3){
            if (nums[0]<nums[1]+nums[2]){
                return nums[0]+nums[1]+nums[2];
            }
            else {nums.erase(nums.begin());}
        }
        return 0;
        

    }
};