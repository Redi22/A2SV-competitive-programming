class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        int countMin = 0;
        vector<int> mins;
        for(int i = 0; i < nums.size(); i++){
            for(int j = 0; j < nums.size(); j++){
                if(nums[j] < nums[i]){
                    countMin++;
                }                
            }
            mins.push_back(countMin);
            countMin = 0;
        }
        return mins;
    }
};