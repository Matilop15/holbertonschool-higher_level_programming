#include "lists.h"
/**
 *check_cycle - check if linked list is a cycle
 *
 *@list: list fot check
 *
 *Return: 1 if is a cycle, 0 if not is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp;

	if (list == NULL)
		return (0);
	while (list)
	{
		tmp = list;
		list = list->next;
		if (tmp <= list)
		return (1);
	}
	return (0);
}
