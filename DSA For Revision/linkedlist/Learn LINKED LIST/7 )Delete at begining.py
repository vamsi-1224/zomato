# Python Function to remove the first node
# of the linked list
def removeFirstNode(head):
    if not head:
        return None
    temp = head

    # Move the head pointer to the next node
    head = head.next
    temp = None
    return head