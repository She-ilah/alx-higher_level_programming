#include "lists.h"

/**
 * check_cycle - Determine if a cycle is present in linked list
 * @list: linked list
 * Return: 1 if cycle is present, 0 if not.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
