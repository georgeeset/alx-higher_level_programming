#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head:head of singly linked list
 *
 * Return: 0 if is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int runner = 0, mover = 0, dif;
	listint_t *ptr = NULL;
	listint_t *run = NULL;

	run = *head;
	ptr = *head;
	if (run == NULL)
		return (1);
	while (run->next)
	{
		runner++;
		run = run->next;
	}
	while (run->n == ptr->n)
	{
		runner--;
		mover++;
		dif = runner - mover;
		if (dif <= 0)
			return (1);
		ptr = ptr->next;
		run = ptr;
		for (; dif > 0; dif--)
			run = run->next;
	}
	return (0);
}
