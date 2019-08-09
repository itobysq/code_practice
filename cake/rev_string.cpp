#include <iostream>
using namespace std;

class Solution {
    public:
        string reverseString(string s) {
            int start = 0;
            int end = s.length() - 1;
            char ch = 0;

        for (; start < end ; start ++, end --)
        {
            ch = s[start];
            s[start] = s[end];
            s[end] = ch;
        }
        return s;
        };
};

int main() {
    Solution sol;
    cout << sol.reverseString("cat")<< endl;
    return 0;
}
