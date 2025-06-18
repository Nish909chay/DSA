typedef struct Node
{
	int data;
	Node *next;
}Node;
typedef struct List
{
	Node *head;
	int size;
}List;

Node *reverseList(List *list)
{
	if(list->head == NULL)
		return NULL;
	Node *curr = list->head;
	Node *prev = NULL;
	while(curr != NULL)
	{
		Node *next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	 list->head = prev; 
	return  list->head;
}