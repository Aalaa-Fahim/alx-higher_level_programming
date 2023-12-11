#include "lists.h"

/**
 * is_palindrome - check if a singly linked list is a palindrome
 * @head: the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
if (head == NULL || *head == NULL)
	return (1);
return (is_palind(head, *head));
}

/**
 * is_palind - check palind or not
 * @head: the head of the list
 * @end: the end of the list
 * Return: 0 if not a palindrome, otherwise 1
 */
int is_palind(listint_t **head, (listint_t *end)
{
if (end == NULL)
	return (1);
if (is_palind(head, end->next) && (*head)->n == end->n)
{
*head = (*head)->next;
return (1);
}
return (0);
}
