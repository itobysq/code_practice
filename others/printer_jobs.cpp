#include <string>
#include <iostream>
#include <unordered_map>

using namespace std;

int jobtime(string jobs) {
    unordered_map<char, int> d;
    int epoch = 0;
    int rest = 2;
    
    for (char ch : jobs) {
        if (d.find(ch) != d.end()) {

            int delta_t = epoch - d[ch];
            int cool = rest + 1 - delta_t;
            if (cool > 0) {
                epoch += cool;

            }
        }
        d[ch] = epoch;
        epoch += 1;
    }
    return epoch;
}

int main() {
    cout << "AAA = " << jobtime("AAA") << endl;
    cout << "ABA = " << jobtime("ABA") << endl;
    return 0;
}
