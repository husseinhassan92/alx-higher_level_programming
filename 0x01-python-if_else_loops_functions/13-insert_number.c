#include "lists.h"

/**
 * insert_node - malloc and insert node into sorted singly linked list
 * @head: pointer to head of linked list
 * @number: data for new node
 * Return: address of new node, or NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = NULL;
	listint_t *node = NULL;

	if (!head)
		return (NULL);

	/* malloc new node */
	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	node->next = NULL;

	/* if no linked list, insert node as the only member */
	if (*head == NULL)
	{
		*head = node;
		(*head)->next = NULL;
		return (node);
	}
	/* if only one node in linked list, do comparision and insert */
	if ((*head)->next == NULL)
	{
		if ((*head)->n < node->n)
			(*head)->next = node;
		else
		{
			node->next = *head;
			*head = node;
		}
		return (node);
	}

	/* if lots of nodes in linked list, do comparision and insert */
	tmp = *head;
	while (tmp->next != NULL)
	{
		/* if new node num is smaller than first node, insert */
		if (node->n < tmp->n)
		{
			node->next = tmp;
			*head = node;
			return (node);
		}
		/* if new node num is the same as an existing node, insert */
		/* compare previous node and next node, insert in between */
		if (((node->n > tmp->n) && (node->n < (tmp->next)->n)) ||
		    (node->n == tmp->n))
		{
			node->next = tmp->next;
			tmp->next = node;
			return (node);
		}
		tmp = tmp->next;
	}
	/* if new node is greatest and never inserted, insert now */
	tmp->next = node;
	return (node);
}
