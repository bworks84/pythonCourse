# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_sorted_lists(list1, list2):
    # Create a dummy node to serve as the head of the merged list
    dummy = ListNode()
    current = dummy  # Pointer to the current node in the merged list

    # Loop until one of the lists is exhausted
    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            current.next = list1
            list1, current = list1.next, list1
        else:
            current.next = list2
            list2, current = list2.next, list2

    # If one of the lists is not exhausted, append the remaining nodes
    if list1 or list2:
        current.next = list1 if list1 else list2

    # Return the head of the merged list (skip the dummy node)
    return dummy.next


# Example usage:
# Assuming list1 and list2 are instances of ListNode representing the head of the sorted linked lists
merged_list_head = merge_sorted_lists([1, 2, 4], [1, 3, 5])


print(merged_list_head)
