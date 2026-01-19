// Reverse Linked List
// Linked List / Two Pointers
// Time Complexity: O(n)
// Space Complexity: O(1)
// leetcode.com/problems/reverse-linked-list/description/

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val ?? 0;
    this.next = next ?? null;
  }
}

const reverseList = (head: ListNode | null): ListNode | null => {
  let prev: ListNode | null = null;
  let current: ListNode | null = head;

  while (current) {
    const next = current.next;
    current.next = prev;
    prev = current;
    current = next;
  }

  return prev;
};

// Test cases
console.log(reverseList(new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))))));
