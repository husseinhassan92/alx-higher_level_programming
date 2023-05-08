#include "lists.h"
/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *p_list, *n_list;

	if (list == NULL || list->next == NULL)
		return (0);

	p_list = list->next;
	n_list = list->next->next;

	while (p_list && n_list && n_list->list)
	{
		if (p_list == n_list)
			return (1);

		p_list = p_list->next;
		n_list = p_list->next->next;
	}

	return (0);
}
