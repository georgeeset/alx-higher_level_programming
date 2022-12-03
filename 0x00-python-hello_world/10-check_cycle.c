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

	point = list;
	if (point)
		fastPoint = point->next;
	while (point && fastPoint)
	{
		if (point == fastPoint)
			return (1);
		point = point->next;
		fastPoint = fastPoint->next;
		if (fastPoint)
			fastPoint = fastPoint->next;
	}
	return (0);
}
