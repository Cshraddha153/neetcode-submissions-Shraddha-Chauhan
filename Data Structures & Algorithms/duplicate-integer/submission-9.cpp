class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // hashset length
        return unordered_set<int>(nums.begin(), nums.end()).size() < nums.size();




        // hashset tc=O(N) sc=O(N)
        // unordered_set<int> seen;
        // for(int num: nums){
        //     if(seen.count(num)){
        //         return true;
        //     }
        //     seen.insert(num);
        // }
        // return false;





        // sorting tc=O(Nlogn) sc=O(1)
        // sort(nums.begin(), nums.end());
        // for(int i=1; i<nums.size(); i++){
        //     if(nums[i]==nums[i-1]){
        //         return true;
        //     }
        // }
        // return false;



        // tc=O(N*N)  sc=O(1)
        // for(int i=0; i<nums.size(); i++){
        //     for(int j=i+1; j<nums.size(); j++){
        //         if(nums[i]==nums[j]){
        //             return true;
        //         }
        //     }
        // }
        // return false;
    }
};