/**
 * Definition for singly-linked list.
 * struct listint_s {
 *     int n;
 *     struct listint_s *next;
 * };
 * typedef struct listint_s listint_t;
 */

int is_palindrome(listint_t **head)
{
    listint_t *slow_ptr = *head;
    listint_t *fast_ptr = *head;
    listint_t *prev_slow_ptr = NULL;
    listint_t *mid_node = NULL;
    listint_t *second_half = NULL;
    int is_palindrome = 1; // initially set to true

    if (*head != NULL && (*head)->next != NULL) {
        /* Find the middle node of the linked list */
        while (fast_ptr != NULL && fast_ptr->next != NULL) {
            fast_ptr = fast_ptr->next->next;
            prev_slow_ptr = slow_ptr;
            slow_ptr = slow_ptr->next;
        }

        /* If there are odd number of elements in the list,
         * skip the middle node */
        if (fast_ptr != NULL) {
            mid_node = slow_ptr;
            slow_ptr = slow_ptr->next;
        }

        /* Reverse the second half of the linked list */
        second_half = slow_ptr;
        prev_slow_ptr->next = NULL; // terminate the first half
        reverse(&second_half);

        /* Compare the first half and second half of the linked list */
        is_palindrome = compare_lists(*head, second_half);

        /* Restore the original linked list */
        reverse(&second_half);
        if (mid_node != NULL) {
            prev_slow_ptr->next = mid_node;
            mid_node->next = second_half;
        } else {
            prev_slow_ptr->next = second_half;
        }
    }

    return is_palindrome;
}

/* Helper function to reverse a linked list */
void reverse(listint_t **head)
{
    listint_t *prev_node = NULL;
    listint_t *current_node = *head;
    listint_t *next_node = NULL;

    while (current_node != NULL) {
        next_node = current_node->next;
        current_node->next = prev_node;
        prev_node = current_node;
        current_node = next_node;
    }

    *head = prev_node;
}

/* Helper function to compare two linked lists */
int compare_lists(listint_t *list1, listint_t *list2)
{
    while (list1 != NULL && list2 != NULL) {
        if (list1->n != list2->n) {
            return 0;
        }
        list1 = list1->next;
        list2 = list2->next;
    }

    return (list1 == NULL && list2 == NULL);
}
