#include <iostream>
using namespace std;

struct Node {
    int item;
    Node *left;
    Node *right;
        int val;
        int left;
        int right;
};

Node build_tree(vector mylist)
{
    if mylist.size() == 0:
        return null

