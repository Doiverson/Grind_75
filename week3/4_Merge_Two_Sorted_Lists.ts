// Merge Two Sorted Lists
// Linked List / Two Pointers
// Time Complexity: O(n + m)
// Space Complexity: O(1)
// leetcode.com/problems/merge-two-sorted-lists/description/

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val ?? 0;
    this.next = next ?? null;
  }
}

/**
 * Merge two sorted linked lists into one sorted linked list.
 * 
 * Best Practices:
 * 1. Use a dummy node to simplify edge cases (empty lists)
 * 2. Iterative approach is preferred over recursive (O(1) space vs O(n+m))
 * 3. Compare values and link nodes in-place
 * 4. Handle remaining nodes after one list is exhausted
 * 
 * Algorithm:
 * - Create a dummy node to serve as the head of the merged list
 * - Use a current pointer to build the merged list
 * - Compare nodes from both lists and attach the smaller one
 * - Continue until one list is exhausted
 * - Attach the remaining nodes from the non-empty list
 */
const mergeTwoLists = (
  list1: ListNode | null,
  list2: ListNode | null
): ListNode | null => {
  // Best Practice 1: Dummy node simplifies edge case handling
  // This avoids special cases for empty lists or initial head selection
  const dummy = new ListNode(0);
  let current: ListNode | null = dummy;

  // Best Practice 2: Iterative approach - O(1) space complexity
  // Compare and merge while both lists have nodes
  while (list1 && list2) {
    if (list1.val <= list2.val) {
      current.next = list1;
      list1 = list1.next;
    } else {
      current.next = list2;
      list2 = list2.next;
    }
    current = current.next;
  }

  // Best Practice 3: Attach remaining nodes
  // One list is exhausted, so attach the rest of the other list
  // This handles cases where lists have different lengths
  current.next = list1 || list2;

  // Return the actual head (skip dummy node)
  return dummy.next;
};

// Alternative: Recursive approach (for educational purposes)
// Note: This uses O(n+m) space due to call stack, but demonstrates recursion
const mergeTwoListsRecursive = (
  list1: ListNode | null,
  list2: ListNode | null
): ListNode | null => {
  /**
   * Recursive approach - cleaner code but uses O(n+m) space.
   * Good for understanding recursion, but iterative is preferred for production.
   */
  if (!list1) return list2;
  if (!list2) return list1;

  if (list1.val <= list2.val) {
    list1.next = mergeTwoListsRecursive(list1.next, list2);
    return list1;
  } else {
    list2.next = mergeTwoListsRecursive(list1, list2.next);
    return list2;
  }
};

// Test cases
// Helper function to create linked list from array
const createList = (values: number[]): ListNode | null => {
  if (values.length === 0) return null;
  const head = new ListNode(values[0]);
  let current = head;
  for (let i = 1; i < values.length; i++) {
    current.next = new ListNode(values[i]);
    current = current.next;
  }
  return head;
};

// Helper function to convert linked list to array for printing
const listToArray = (head: ListNode | null): number[] => {
  const result: number[] = [];
  let current = head;
  while (current) {
    result.push(current.val);
    current = current.next;
  }
  return result;
};

// Test case 1: Both lists have elements
const list1 = createList([1, 2, 4]);
const list2 = createList([1, 3, 4]);
const merged1 = mergeTwoLists(list1, list2);
console.log(`Test 1: [${listToArray(merged1).join(", ")}]`); // Expected: [1, 1, 2, 3, 4, 4]

// Test case 2: One list is empty
const list3 = createList([]);
const list4 = createList([0]);
const merged2 = mergeTwoLists(list3, list4);
console.log(`Test 2: [${listToArray(merged2).join(", ")}]`); // Expected: [0]

// Test case 3: Both lists are empty
const list5 = createList([]);
const list6 = createList([]);
const merged3 = mergeTwoLists(list5, list6);
console.log(`Test 3: [${listToArray(merged3).join(", ")}]`); // Expected: []

// Test case 4: Lists with different lengths
const list7 = createList([1, 3, 5, 7]);
const list8 = createList([2, 4]);
const merged4 = mergeTwoLists(list7, list8);
console.log(`Test 4: [${listToArray(merged4).join(", ")}]`); // Expected: [1, 2, 3, 4, 5, 7]
