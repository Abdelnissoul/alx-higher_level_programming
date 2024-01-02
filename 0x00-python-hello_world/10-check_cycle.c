#include "lists.h"
/**
 * check_cycle - checks if list is cyclical or not
 * @list: pointer to the head of list for checking
 * Return: 0 if there is no cycle, otherwise 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
