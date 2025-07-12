#include<stdio.h>
#include<stdbool.h>

typedef struct Node
{
    int data;
    struct Node *next;
}Node;

void init(Node **head)
{
    *head = NULL;
}

int main()
{
    Node *head;
    init(&head);
}

/*
141. Linked List Cycle
Easy

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
*/

bool hasCycle(Node *head)
{
    Node *left = head;
    Node *right = head;

    while(right != NULL && right->next != NULL)
    {
        // first increment the pointers or else they at start point to the same location 
        left = left->next;
        right = right->next->next;

        if(left == right)
        {
            return 1;
        }
    }
    return 0;
}
