# Python function to find the length of the linked list
def find_length(head):
  
    # Initialize a counter for the length
    length = 0

    # Start from the head of the list
    current = head

    # Traverse the list and increment the length for each
    # node
    while current is not None:
        length += 1
        current = current.next

    # Return the final length of the linked list
    return length