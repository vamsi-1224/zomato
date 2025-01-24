# Python Function to remove the last node of the linked list
def removeLastNode(head):
    # If the list is empty, return None
    if head is None:
        return None

    # If the list has only one node, delete it and return None
    if head.next is None:
        head = None
        return None

    # Find the second last node
    second_last = head
    while second_last.next.next is not None:
        second_last = second_last.next

    # Remove the last node
    second_last.next = None

    # Return the modified list
    return head