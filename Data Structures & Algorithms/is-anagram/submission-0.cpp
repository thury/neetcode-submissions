class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> freq;
        for (char c : s) {
            auto k = freq.find(c);
            if (k == freq.end()) {
                freq.insert({c, 1});
                continue;
            }
            k->second = k->second + 1;
        }
        for (char c : t) {
            auto k = freq.find(c);
            if (k == freq.end()) {
                return false;
            }
            k->second = k->second - 1;
            if (k -> second == 0) {
                freq.erase(k);
                continue;
            }
        }
        return freq.empty();
    }
};
