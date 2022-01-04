#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * is_palindrome - checks if is a palindrome.
 * @head: pointer head node.
 * Return: 0 if not a palindrome, 1 if is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	int a = 0;

	listint_t *temp = *head;

	if (*head == NULL)
		return (0);
	*head = temp->next;
	a = temp->n;
	a = a + 1;
	free(temp);
	return (a);
}
