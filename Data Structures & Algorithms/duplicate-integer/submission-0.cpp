class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> hash;
        for (int a : nums) {
            if (hash.find(a) == hash.end()) hash.insert({a, 1});
            else return true;
        }
        return false;
    } 
};
