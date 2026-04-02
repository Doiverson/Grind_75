# Linked List Cycle
# Linked List / Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
# leetcode.com/problems/linked-list-cycle/description/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head: ListNode) -> bool:
    fast = head
    while fast and fast.next and head:
        head = head.next
        fast = fast.next.next
        if head is fast:
            return True
    return False


# Test cases
if __name__ == "__main__":
    # Test case 1: Has cycle [3,2,0,-4], pos=1
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next  # cycle to index 1
    print(hasCycle(head))  # Expected: True

    # Test case 2: No cycle [1,2]
    head2 = ListNode(1)
    head2.next = ListNode(2)
    print(hasCycle(head2))  # Expected: False

    # Test case 3: Single node, no cycle
    head3 = ListNode(1)
    print(hasCycle(head3))  # Expected: False
