#include<stdio.h>
#include<stdlib.h>
typedef struct Node
{
	int data;
	struct Node *next,*prev;
}Node;
typedef struct LL
{
	Node *head;
	int size;
}LL;

void init(LL *list)
{
	list->head = NULL;
	list->size=0;
}
void insertStart(LL *list, int data)
{
	Node *nn = (Node*)malloc(sizeof(struct Node));
	nn->data=data;
	nn->next = list->head;
	nn->prev = NULL;
	list->head = nn;
	list->size++;
}
void insertLast(LL *list, int data)
{
	if(list->head == NULL)
	{
		insertStart(list, data);
		return;
	}
	Node *nn = (Node*)malloc(sizeof(struct Node));
	nn->data = data;
	list->size++;
	nn->next = NULL;
	Node *curr = list->head;
	while(curr->next != NULL)
		curr = curr->next;
	nn->next = NULL;
	nn->prev =curr;
	curr->next = nn;
}

void show(LL *list)
{
	Node *curr = list->head;
	printf("\n");
	while(curr != NULL)
	{
		printf("%d -> ",curr->data);
		curr = curr->next;
	}
	printf("\n");
}

void deleteFirst(LL *list)
{
	if(list->head  == NULL)
		return;
	Node *curr = list->head;
	list->head = curr->next;
	if(curr->next != NULL)
	{
		curr->next->prev = NULL;
	}
	free(curr);
	list->size--;
}
void deleteLast(LL *list)
{
	if(list->head  == NULL)
		return;
	Node *curr = list->head;
	if(curr->next == NULL)
	{
		free(curr);
		list->head = NULL;
		list->size--;
		return;
	}
	while(curr->next == NULL)
		curr = curr->next;
	
	Node *temp = curr->next;
	curr->next = NULL;
	free(temp);
	list->size--;
}

void insertSpecific(LL *list, int data, int pos)
{
	if(list->head == NULL)
	{
		insertStart(list,data);
		return;
	}
	if(pos > list->size)
	{
		printf("\nposition greater than size");
		return;
	}
	Node *nn = (Node*)malloc(sizeof(struct Node));
	nn->data = data;
	Node *curr = list->head;
	int i=1;
	while(curr != NULL && i<pos-1)
	{
		i++;
		curr = curr->next;
	}
	Node *temp = curr->next;
	curr->next = nn;
	nn->next = temp;
	temp->prev = nn;
	nn->prev = curr;
	

}

void deleteSpecific(LL *list,int pos)
{
	if(list->head == NULL)
	{
		printf("\n List empty");
		return;
	}
	if(pos > list->size)
	{
		printf("\nposition greater than size");
		return;
	}
	Node *curr = list->head;
	int i=1;
	while(curr->next != NULL && i<pos-1)
	{
		i++;
		curr = curr->next;
	}
	Node *temp = curr->next;
	temp->next->prev = curr;
	curr->next = temp->next;
	free(temp);
	
}

int main()
{
	LL list;
	init(&list);
	insertStart(&list,2);
	insertStart(&list,1);
	insertLast(&list,4);
	show(&list);
	insertSpecific(&list,3,3);
	show(&list);
	deleteSpecific(&list,2);
	show(&list);
	

	return 0;
}