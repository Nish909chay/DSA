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
---------------------------------------------------------------------------------------------------------------------------------------------

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


21. Merge Two Sorted Lists
Easy
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
------------------------------------------------------------------------------------------------------------------------

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) 
{
        if(list1 == NULL && list2 == NULL)
            return NULL;
        if(list1 == NULL)
            return list2;
        if(list2 == NULL)
            return list1;

        struct ListNode *curr = list1;
        while(curr->next != NULL)
        {
            curr = curr->next;
        }
        curr->next = list2;

        return list1;
}
---------------------------------------------------------------------------------------------

21. Merge Two Sorted Lists
Node* merge(Node* list1,Node* list2) 
{
    if(list1 == NULL)
        return list2;
    else if(list2 == NULL)
        return list1;

    if(list1->val <= list2->val)
    {
        list1->next = merge(list1->next, list2);
        return list1;
    }
    else if(list1->val >= list2->val)
    {
        list2->next = merge(list1, list2->next);
        return list2;
    }
}
*/

/*
876. Middle of the Linked List
Easy

Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3
---------------------------------------------------
struct ListNode* middleNode(struct ListNode* head) 
{
    struct ListNode *fast = head;
    struct ListNode *slow = head;

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        slow = slow->next;
    }

    return slow;
}
*/

/*
19. Remove Nth Node From End of List
Medium
Given the head of a linked list, remove the nth node from the end of the list and return its head.
--------------------------------------------------------------------------------------------------
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) 
{
    struct ListNode dummy;
    dummy.next = head;
    struct ListNode *fast = &dummy;
    struct ListNode *slow = &dummy;

    for (int i = 0; i <= n; i++) 
    {
        if (fast == NULL) 
            return dummy.next;  
        fast = fast->next;
    }

    while(fast != NULL)
    {
        fast = fast->next;
        slow = slow->next;
    }

    struct ListNode *temp = slow->next;
    slow->next = temp->next;
    free(temp); 

    return dummy.next;
}

*/


