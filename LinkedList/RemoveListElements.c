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

Node *removeListElement(List *list, int data)
{
	while(list->head != NULL && head->data == data)
	{
		Node *temp = list->head;
		list->head = temp->next;	
		free(temp);
	}
	Node *curr = list->head;
	while(curr != NULL && curr->next != NULL)  	// to prevent segemntation fault cuz in the loop you access curr->next->data but if curr->next = 								//  NULL THEN segmentation error
	{
		if(curr->next->data == data)
		{
			Node *temp = curr->next;
			curr->next = temp->next;
			free(temp);
		}
		else{
			curr = curr->next;		//very important dry run 1,2,2,3 and see with and without else
		}
	}
	
}