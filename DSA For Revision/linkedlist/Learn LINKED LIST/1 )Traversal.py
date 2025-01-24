# Python Function to traverse and print the elements of the linked list
def traverse_linked_list(head):
    # Start from the head of the linked list
    current = head

    # Traverse the linked list until reaching the end (None)
    while current is not None:

        # Print the data of the current node followed by a space
        print(current.data),

        # Move to the next node
        current = current.next

    print()  # Print a new line after traversing the linked list