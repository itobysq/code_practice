#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    unordered_map<string, int> lighthours;
    lighthours.insert(make_pair("incandescent", 1200));
    lighthours.insert(make_pair("compact floursecent", 10000));
    lighthours.insert(make_pair("LED", 50000));

    for (auto& element: lighthours)
    {
        cout << element.first << " :: " << element.second << endl;
    }
    return 0;
}
