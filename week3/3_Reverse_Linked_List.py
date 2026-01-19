# Reverse Linked List
# Linked List / Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
# leetcode.com/problems/reverse-linked-list/description/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:
    prev = None
    current = head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev


# Test cases
if __name__ == "__main__":
    # Test case 1: Basic operations
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(reverseList(head))
