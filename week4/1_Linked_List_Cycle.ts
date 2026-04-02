// Linked List Cycle
// Linked List / Two Pointers
// Time Complexity: O(n)
// Space Complexity: O(1)
// leetcode.com/problems/linked-list-cycle/description/

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val ?? 0;
    this.next = next ?? null;
  }
}

const hasCycle = (head: ListNode | null): boolean => {
  let fast = head;
  while (fast && fast.next && head) {
    head = head.next!;
    fast = fast.next.next;
    if (head === fast) return true;
  }

  return false;
};

// ベストプラクティス: Floyd's Cycle Detection（亀とウサギのアルゴリズム）
// slow と fast を明示的に分けることで、意図が明確になる
const hasCycleBest = (head: ListNode | null): boolean => {
  // slow: 1歩ずつ進むポインタ（亀）
  let slow = head;
  // fast: 2歩ずつ進むポインタ（ウサギ）
  let fast = head;

  // fast と fast.next が存在する限りループ
  // fast が null に到達 → リストの終端 → サイクルなし
  while (fast && fast.next) {
    // slow を1歩進める
    slow = slow!.next;
    // fast を2歩進める
    fast = fast.next.next;

    // 2つのポインタが同じノードを指す → サイクルが存在
    if (slow === fast) return true;
  }

  // ループ終了 = fast が終端に到達 = サイクルなし
  return false;
};

// Test cases
// Test case 1: Has cycle [3,2,0,-4], pos=1
const head = new ListNode(3);
head.next = new ListNode(2);
head.next.next = new ListNode(0);
head.next.next.next = new ListNode(-4);
head.next.next.next.next = head.next; // cycle to index 1
console.log(hasCycle(head)); // Expected: true
console.log(hasCycleBest(head)); // Expected: true

// Test case 2: No cycle [1,2]
const head2 = new ListNode(1, new ListNode(2));
console.log(hasCycle(head2)); // Expected: false
console.log(hasCycleBest(head2)); // Expected: false

// Test case 3: Single node, no cycle
const head3 = new ListNode(1);
console.log(hasCycle(head3)); // Expected: false
console.log(hasCycleBest(head3)); // Expected: false
