#include <iostream>

using namespace std;

struct node{
    int data;
    node* left;
    node* right;
};

struct node* allocate(int data){
    node* pNode = (node*)malloc(sizeof(node));
    pNode -> left = nullptr;
    pNode -> right = nullptr;
    pNode -> data = data;

    return pNode;
}

void insert(node* root, node* newNode);
void destruct(struct node** root);
void mirror(node *root);
int size(node* root);
void preOrder(node* root);
void inOrder(node* root);
void postOrder(node* root);
int height(node* root);
int sumOfWeight(node* root);
int maxPathWeight(node* root);


int main(){
    int numTestCases;
    scanf("%d", &numTestCases);
    while (numTestCases--){
        int num , head;
        cin >> num >> head;
        node* root = allocate(head);
        
        for (int i = 0; i < num-1; i++){
            int data;
            cin >> data;
            node* newNode = allocate(data);
            insert(root, newNode);
            }
        cout << size(root) << endl;
        cout << height(root) << endl;
        cout << sumOfWeight(root) << endl;
        cout << maxPathWeight(root) << endl;
        mirror(root);
        preOrder(root); printf("\n");
        inOrder(root); printf("\n");
        postOrder(root); printf("\n");
        destruct(&root);
        if (root == NULL)
            printf("0\n");
        else
            printf("1\n");
    }
    return 0;
}


void insert(node* root, node* newNode){  
    if(root -> data > newNode -> data ){
        if(root -> left)
            insert(root->left, newNode);
        else
            root -> left = newNode;
    }
    else if(root -> data < newNode -> data ){
         if(root -> right)
            insert(root->right, newNode);
        else
            root -> right = newNode;
    }

}


void preOrder(node* root){
    if(root == NULL)
        return;
    else{
        cout << root -> data << " ";
        preOrder(root->left);
        preOrder(root-> right);
    }
}

void inOrder(node* root){
    if(root == NULL)
        return;
    else{
        inOrder(root->left);
        cout << root -> data << " ";
        inOrder(root-> right);
    }
}

void postOrder(node* root){
    if(root == NULL)
        return;
    else{
        postOrder(root->left);
        postOrder(root-> right);
        cout << root -> data << " ";
    }
}
void postOrder2(node* root){
    if(root == NULL)
        return;
    else{
        postOrder2(root->left);
        postOrder2(root-> right);
    }
}

int size(node* root){
    if(root == NULL)
        return 0;
    else{
        return size(root->left) + 1 + size(root->right);
    }
}


int height(node* root){
    if(root == NULL)
        return -1;
    else{
        int rt = height(root -> right);
        int lf = height(root -> left);

        if(lf >= rt){
            return lf +1;}
        else {
            return rt + 1;}
    }

}

int sumOfWeight(node* root){
    if(root == NULL)
        return 0;
    else
        return sumOfWeight(root->left) + sumOfWeight(root->right)+root->data;
}


int maxPathWeight(node *root){
    if(root == NULL)
        return 0;
    else 
        return root -> data + max(maxPathWeight(root -> left), maxPathWeight(root -> right));
}

void mirror(node *root)
{
    if (root == NULL)
        return;
    else
    {
        struct node *temp;

        mirror(root->left);
        mirror(root->right);

        temp = root->left;
        root ->left = root->right;
        root->right = temp;
    }
}


void destruct(node** root){
    if((*root) -> left)
        postOrder2((*root) -> left);
    if((*root) -> right)
        postOrder2((*root) -> right);
    *root = NULL;
    free(*root);

}
