# Merge Two Sorted Lists
# Linked List / Two Pointers
# Time Complexity: O(n + m)
# Space Complexity: O(1)
# leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Best Practice 1: Dummy node simplifies edge case handling
        # This avoids special cases for empty lists or initial head selection
        dummy = ListNode(0)
        current = dummy

        # Best Practice 2: Iterative approach - O(1) space complexity
        # Compare and merge while both lists have nodes
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Best Practice 3: Attach remaining nodes
        # One list is exhausted, so attach the rest of the other list
        # This handles cases where lists have different lengths
        current.next = list1 if list1 else list2

        # Return the actual head (skip dummy node)
        return dummy.next


# Alternative: Recursive approach (for educational purposes)
# Note: This uses O(n+m) space due to call stack, but demonstrates recursion
def mergeTwoListsRecursive(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    """
    Recursive approach - cleaner code but uses O(n+m) space.
    Good for understanding recursion, but iterative is preferred for production.
    """
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.val <= list2.val:
        list1.next = mergeTwoListsRecursive(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoListsRecursive(list1, list2.next)
        return list2


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Helper function to create linked list from list
    def create_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    # Helper function to convert linked list to list for printing
    def list_to_array(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    # Test case 1: Both lists have elements
    list1 = create_list([1, 2, 4])
    list2 = create_list([1, 3, 4])
    merged = solution.mergeTwoLists(list1, list2)
    print(f"Test 1: {list_to_array(merged)}")  # Expected: [1, 1, 2, 3, 4, 4]

    # Test case 2: One list is empty
    list1 = create_list([])
    list2 = create_list([0])
    merged = solution.mergeTwoLists(list1, list2)
    print(f"Test 2: {list_to_array(merged)}")  # Expected: [0]

    # Test case 3: Both lists are empty
    list1 = create_list([])
    list2 = create_list([])
    merged = solution.mergeTwoLists(list1, list2)
    print(f"Test 3: {list_to_array(merged)}")  # Expected: []

    # Test case 4: Lists with different lengths
    list1 = create_list([1, 3, 5, 7])
    list2 = create_list([2, 4])
    merged = solution.mergeTwoLists(list1, list2)
    print(f"Test 4: {list_to_array(merged)}")  # Expected: [1, 2, 3, 4, 5, 7]
