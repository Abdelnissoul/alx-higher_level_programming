#include "lists.h"

/**
 * is_palindrom - checks if a singly linked list is a palindrome
 * @head: pointer to a pointer that points to the head of list
 *
 * Return: 0 if not palindrome, 1 if yes
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (isit_palin(head, *head));
}

/**
 * isit_palin - checks if is it palindrome
 * @head: pointer to pointer to head
 * @last: last element in list
 * Return: 1 if yes otherwise 0
 */
int isit_palin(listint_t **head, listint_t *last)
{
	if (last == NULL)
		return (1);

	if (isit_palin(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
