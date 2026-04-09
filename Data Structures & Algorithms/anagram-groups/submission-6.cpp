#include <vector>
#include <unordered_map>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // sorting   tc=O(M*NlogN) sc=O(M*N)
        unordered_map<string, vector<string>> res;
        for(const auto& s: strs){
            string sortedS = s;
            sort(sortedS.begin(), sortedS.end());
            res[sortedS].push_back(s);
        }

        vector<vector<string>> result;
        for(auto& pair:res){
            result.push_back(pair.second);
        }
        return result;





        //  Hashtable tc=O(M*N)  sc=O(m) o/p= list=O(M*N)
        // unordered_map<string, vector<string>> res;
        // for(const auto&s: strs){
        //     vector<int> count(26, 0);
        //     for(char c: s){
        //         count[c-'a']++;
        //     }
            
        //     string key = to_string(count[0]);
        //     for(int i=1; i<26; i++){
        //         key += ',' + to_string(count[i]);
        //     }
        //     // cout<<"key = "<<key<<endl;
        //     res[key].push_back(s);
        // }

        // vector<vector<string>> result;
        // for(const auto& pair: res){
        //     result.push_back(pair.second);
        // }
        // return result;
    }
};
