#include <stdlib.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

/**
 * check_cycle - check if a loop exist
 *
 * @list: linked list
 *
 * Return: 1 has no cycle otherwise it has
*/

int check_cycle(listint_t *list)
{
	listint_t *slow_p = list, *fast_p = list;

	while (slow_p && fast_p && fast_p->next)
	{
	slow_p = slow_p->next;
	fast_p = fast_p->next->next;
	if (slow_p == fast_p)
	{
		return (1);
	}
	}
	return (0);
}
