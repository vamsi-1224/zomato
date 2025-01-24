# Python function to search for a value in the Linked List
def search_linked_list(head, target):

    # Traverse the Linked List
    while head is not None:

        # Check if the current node's data matches the target value
        if head.data == target:

            return True  # Value found
        # Move to the next node
        head = head.next

    return False  # Value not found