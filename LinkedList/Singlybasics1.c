#include <stdio.h>
#include <stdlib.h>

typedef struct Node 
{
    int data;
    struct Node *next;
} Node;

typedef struct stack
{
    int top;
    int arr[50];
} stack;

void init(Node **head)
{
    *head = NULL;
}

int isEmpty(Node **head)
{
    return (*head == NULL);
}

int nodes(Node **head)
{
    Node *curr = *head;
    int n = 0;
    while (curr != NULL)
    {
        n++;
        curr = curr->next;
    }
    return n;
}


void insertSpecific(Node **head, int data, int pos)
{
    Node *nn = (Node *)malloc(sizeof(Node));
    nn->data = data;
    nn->next = NULL;

    if (isEmpty(head) || pos == 1)
    {
        nn->next = *head;
        *head = nn;
        return;
    }

    int size = nodes(head);
    if (pos > size + 1)
    {
        printf("\nPosition greater than list size\n");
        free(nn);
        return;
    }

    Node *curr = *head;
    int i = 1;
    while (i < pos - 1 && curr != NULL)
    {
        i++;
        curr = curr->next;
    }

    nn->next = curr->next;
    curr->next = nn;
}

void deleteSpecific(Node **head, int pos)
{
    if (*head == NULL)
    {
        printf("\nNothing to remove. List is empty.\n");
        return;
    }

    if (pos == 1)
    {
        Node *curr = *head;
        *head = curr->next;
        free(curr);
        return;
    }

    int size = nodes(head);
    if (pos > size)
    {
        printf("\nPosition greater than list size\n");
        return;
    }

    Node *curr = *head;
    int i = 1;
    while (i < pos - 1 && curr != NULL)
    {
        i++;
        curr = curr->next;
    }

    Node *target = curr->next;
    curr->next = target->next;
    free(target);
}

void show(Node **head)
{
    Node *curr = *head;
    printf("\nList:\n");
    while (curr != NULL)
    {
        printf("%d->", curr->data);
        curr = curr->next;
    }
    printf("NULL\n");
}

void reverseList(Node **head)
{
	if (*head == NULL)
   	 {
       		 printf("\nNothing to remove. List is empty.\n");
        		return;
   	 }
	Node *curr = *head;
	Node *prev = NULL;
	while(curr != NULL)
	{
		Node *next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	*head = prev;
}

int main()
{
    Node *head;
    init(&head);

    insertSpecific(&head, 5, 1);
    insertSpecific(&head, 4, 1);
    insertSpecific(&head, 3, 1);
    insertSpecific(&head, 2, 1);
    insertSpecific(&head, 1, 1);
    show(&head);
    reverseList(&head);
    show(&head);
    return 0;
}
