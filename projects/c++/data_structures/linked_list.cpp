#include <iostream>

struct Node{
    int value;
    Node* next;
};

class LinkedList{
private:
    Node* head;
public:
    LinkedList(){
        head = nullptr;
    }

    //Insert function
    bool insert(int value){
        if (head == nullptr){
            Node* newNode = new Node;
            newNode->value = value;
            newNode->next = nullptr;
            head = newNode;
            return true;
        }
        else{
            Node* current = head;
            Node* previous = head;

            while(current->next != nullptr && value > current->value){
                previous = current;
                current = current->next;
            }

            if(current == head){
                Node* newNode = new Node;
                newNode->value = value;
                newNode->next = head;
                head = newNode;
                return true;
            }
            else if(current->next == nullptr){
                Node* newNode = new Node;
                newNode->value = value;
                newNode->next = nullptr;
                current->next = newNode;
                return true;
            }
            else{
                Node* newNode = new Node;
                newNode->value = value;
                newNode->next = current;
                previous->next = newNode;
                return true;
            }
        }

    }

    bool remove(int value){
        Node* previous = head;
        Node* current = head;

        while(current->next != NULL && current->value != value){
            previous = current;
            current = current->next;
        }

        if(current->value == value){
            if (current == head){
                Node* nodeToDelete = head;
                head = head->next;
                delete nodeToDelete;
                return true;
            }
            else if (current->next == nullptr){
                Node* nodeToDelete = current;
                previous->next = nullptr;
                delete nodeToDelete;
                return true;
            }
            else{
                Node* nodeToDelete = current;
                previous->next = current->next;
                delete nodeToDelete;
                return true;
            }
        }
        else{
            return false;
        }
    }

    void printList(){
        Node* current = head;
        while(current != nullptr){
            std::cout << current->value << " ";
            current = current->next;
        }
        std::cout << "\n";
    }

};

int main(){
    LinkedList my_list;

    my_list.insert(5);
    my_list.insert(3);
    my_list.insert(2);
    my_list.insert(7);

    my_list.printList();

    my_list.remove(2);

    my_list.printList();
}