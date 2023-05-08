#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *p_list = list;
	listint_t *n_list = list;

	if (!list)
		return (0);

	while (1)
	{
		/*traverse through nodes as long as linked list node exists*/
		if (p_list->next != NULL && p_list->next->next != NULL)
		{
			p_list = p_list->next->next;
			n_list = n_list->next;

			if (p_list == n_list) /*if nodes match, cycle found*/
				return (1);
		}
		else
			return (0);
	}

}
