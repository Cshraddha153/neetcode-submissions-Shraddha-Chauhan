class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // hashmap (one pass) tc=O(N)  sc=O(N)
        int n = nums.size();
        unordered_map<int, int> prevMap; // number-->index

        for(int i=0; i<n; i++){
            int diff = target - nums[i];
            if(prevMap.find(diff) != prevMap.end()){
                return {prevMap[diff], i};
            }
            prevMap.insert({nums[i], i});
        }



        // brute force tc=O(N2) sc=O(1)
        // for(int i=0; i<nums.size(); i++){
        //     for(int j=i+1; j<nums.size(); j++){
        //         if(nums[i]+nums[j]==target){
        //             return {i, j};
        //         }
        //     }
        // }
        return {};
    }
};
