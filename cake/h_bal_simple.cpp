struct Node {
    std::string data;
    Node *left;
    Node *right;

    Node(int data) {
        data = d;
        left = l;
        right = r;
    }
};

static std:vector<const Node *> postorder(Node *root) {
    std::vector<const Node *> result;
    
