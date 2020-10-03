#include<iostream>

struct Node{
    int data;
    Node* leftChild;
    Node* rightChild;
};

class Tree{
private:
    Node* root = NULL;

    //Insert function===========================================================================
    bool pInsert(Node* curr, int dataToInsert){
        if (curr->data == dataToInsert){
            return false;
        }

        if (dataToInsert < curr->data){
            if (curr->leftChild == NULL){
                Node* newNode = new Node();
                newNode->data = dataToInsert;
                newNode->leftChild = NULL;
                newNode->rightChild = NULL;

                curr->leftChild = newNode;
                return true;
            }
            else{
                return pInsert(curr->leftChild, dataToInsert);
            }
        }
        else{
            if (curr->rightChild == NULL){
                Node* newNode = new Node();
                newNode->data = dataToInsert;
                newNode->leftChild = NULL;
                newNode->rightChild = NULL;

                curr->rightChild = newNode;
                return true;
            }
            else{
                return pInsert(curr->rightChild, dataToInsert);
            }
        }
    }

    //inOrderSuccNode helper function===================================================================
    Node* inOrderSuccNode(Node* curr){
        while(curr->rightChild != NULL){
            curr = curr->rightChild;
        }
        return curr;
    }

    //inOrderSuccVal helper function===============================================================
    int inOrderSuccVal(Node* curr){
        while(curr->rightChild != NULL){
            curr = curr->rightChild;
        }
        return curr->data;
    }

    //Remove function==========================================================================
    bool pRemove(Node* curr, Node* prev, int dataToRemove){

        //First case is if root is null-----------------
        if(curr == NULL){
            return false;
        }

        //Second case deleteing node with no children------------
        if(curr->data == dataToRemove && curr->leftChild == NULL && curr->rightChild == NULL){
            
            Node* nodeToDelete = curr;

            //check if curr node is root node
            if(curr == root){
                root = NULL;
                delete nodeToDelete;
                return true;
            }
            
            //otherwise determine which child of the prev node curr is
            if(curr == prev->leftChild){//curr is left child of prev
                
                prev->leftChild = NULL;
                delete nodeToDelete;
                return true;
            }
            else{//curr is right child of prev
                prev->rightChild = NULL;
                delete nodeToDelete;
                return true;
            }
        }

        //Third case is deleting a node with one child------------
        //Node only has left child
        if(curr->data == dataToRemove && curr->leftChild != NULL && curr->rightChild == NULL){
            
            Node* nodeToDelete = curr;

            //check if curr node is root node
            if(curr == root){
                root = curr->leftChild;
                delete nodeToDelete;
                return true;
            }

            //Otherwise determine which child of the prev node curr is
            if(curr == prev->leftChild){//curr is left child of prev
                prev->leftChild = curr->leftChild;
                delete nodeToDelete;
                return true;
            }
            else{//curr is right child of prev
                prev->rightChild = curr->leftChild;
                delete nodeToDelete;
                return true;
            }
            
        }

        //Node only has right child
        if(curr->data == dataToRemove && curr->leftChild == NULL && curr->rightChild != NULL){
            
            Node* nodeToDelete = curr;
            
            //check if curr node is root node
            if(curr == root){
                root = curr->rightChild;
                delete nodeToDelete;
                return true;
            }

            //Otherwise determine which child of the prev node curr is
            if(curr->data < prev->data){//curr is left child of prev
                prev->leftChild = curr->rightChild;
                delete nodeToDelete;
                return true;
            }
            else{//curr is right child of prev
                prev->rightChild = curr->rightChild;
                delete nodeToDelete;
                return true;
            }
            
        }

        //Forth case is deleteing a node with 2 child nodes--------------------
        if(curr->data == dataToRemove && curr->leftChild != NULL && curr->rightChild != NULL){
            //get the in order successor to be the new value of the node
            curr->data = inOrderSuccVal(curr->leftChild); 
            //call the function on the left node to delete the node that
            //had its value copied into the curr node. This will recursively 
            //run until the list is properly ordered again.
            return pRemove(curr->leftChild, curr, curr->data); 

        }

        // //Traverse in order
        bool left = pRemove(curr->leftChild, curr, dataToRemove);
        bool right = pRemove(curr->rightChild, curr, dataToRemove);

        if(left || right){
            return true;
        }
        return false;
    }

    //In order traversal=======================================================================
    void pInorder(Node* curr){
        if (curr != NULL){
            if(curr->leftChild != NULL){
                pInorder(curr->leftChild);
            }

            std::cout << curr->data << std::endl;

            if(curr->rightChild != NULL){
                pInorder(curr->rightChild);
            }
        }
        return;
    }

    //Post order traversal=====================================================================
    void pPostorder(Node* curr){
        if (curr != NULL){
            if(curr->leftChild != NULL){
                pInorder(curr->leftChild);
            }

            if(curr->rightChild != NULL){
                pInorder(curr->rightChild);
            }

            std::cout << curr->data << std::endl;
        }
        return;
    }

    //Pre order tranversal=====================================================================
    void pPreorder(Node* curr){
        if (curr != NULL){
            std::cout << curr->data << std::endl;

            if(curr->leftChild != NULL){
                pInorder(curr->leftChild);
            }

            if(curr->rightChild != NULL){
                pInorder(curr->rightChild);
            }

        }
        return;
    }

public:
    Tree(){
        root = new Node();
        root->leftChild = NULL;
        root->rightChild = NULL;
    }

    Tree(int val){
        root = new Node();
        root->data = val;
        root->leftChild = NULL;
        root->rightChild = NULL;
    }

    bool insert(int dataToInsert){
        return pInsert(root, dataToInsert);
    }

    bool remove(int dataToRemove){
        return pRemove(root, root, dataToRemove);
    }

    void printRoot(){
        std::cout << root->data << std::endl;
    }

    void postorder(){
        pPostorder(root);
    }

    void preorder(){
        pPreorder(root);
    }

    void inorder(){
        pInorder(root);
    }
  
};

int main(){
    Tree myTree(5);
    
    myTree.insert(6);
    myTree.insert(4);
    myTree.insert(7);
    myTree.insert(3);
    myTree.insert(8);
    myTree.insert(2);
    myTree.insert(9);
    myTree.insert(1);
    myTree.insert(10);
    myTree.insert(0);

    myTree.inorder();

    int num = 5;

    std::cout << "\nSuccessfully removed " << num << " T(1) or F(0): " << myTree.remove(num) << "\n";

    myTree.inorder();
}