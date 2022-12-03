#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - check if a singly linked list has a cycle in it
 * @list: head of linked list
 *
 * Return: 0 if there is no cycle or 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *point = NULL, *fastPoint = NULL;

	point = fastPoint = list;
	while (point && fastPoint)
	{
		point = point->next;
		fastPoint = fastPoint->next;
		if (fastPoint)
			fastPoint = fastPoint->next;
		if (point == fastPoint)
			return (1);
	}
	return (0);
}
