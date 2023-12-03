#include <stdlib>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: the address of the head pointer
 * @number: number to insert
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *next = malloc(sizeof(listint_t));

	if (!next)
		return (NULL);

	next->n = number;
	next->new = NULL;

	if (!node || next->n < node->n)
	{
		next->new = node;
		return (*head = next);
	}

	while (node)
	{
		if (!node->new || next->n < node->new->n)
		{
			next->new = node->new;
			node->new = next;
			return (node);
		}
		node = node->new;
	}
	return (NULL);
}
