#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
/**
 * insert_node - inserts a number into a sotred singly linked list
 * @head: first item in list
 * @number: integer to add to list items
 * Return: Null if failed or address of new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *point;
	listint_t *newNode;
	listint_t *prev = NULL;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;
	newNode->next = NULL;
	point = *head;
	while (point)
	{
		if (prev)
		{
			if (prev->n <= number && point->n >= number)
			{
				prev->next = newNode;
				newNode->next = point;
				return (newNode);
			}
		}
		else
		{
			if (point->n > number)
			{
				newNode->next = point;
				*head = newNode;
				return (newNode);
			}
		}
		prev = point;
		point = point->next;
	}
	prev->next = newNode;
	return (newNode);
}
