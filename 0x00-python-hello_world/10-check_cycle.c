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
	listint_t *point = NULL;
	int j = 0, k;
	listint_t **len;

	len = malloc(sizeof(listint_t *));
	if (len == NULL)
		exit(0);
	point = list;
	while (point)
	{
		if (j > 0)
		{
			for (k = 0; k < j; k++)
			{
				if (point == len[k])
				{
					return (1);
				}
			}
		}
		len[j] = point;
		j++;
		len = realloc(len, sizeof(listint_t *) * (j + 1));
		point = point->next;
	}
	return (0);
}
