# Implement Queue using Stacks
# Approach: Two Stacks (Input Stack + Output Stack)
#
# Key Insight:
# - Stack is LIFO (Last In First Out)
# - Queue is FIFO (First In First Out)
# - To convert LIFO to FIFO, we use two stacks:
#   1. Input stack: stores elements as they're pushed
#   2. Output stack: stores elements in reverse order for popping
#
# Algorithm:
# - push(x): Add to input stack (O(1))
# - pop(): If output stack is empty, transfer all from input to output, then pop from output
# - peek(): Same as pop but don't remove the element
# - empty(): Both stacks must be empty
#
# Time Complexity:
#   - push: O(1) - direct append
#   - pop: O(1) amortized - each element moved at most once from input to output
#   - peek: O(1) amortized - same as pop
#   - empty: O(1) - simple length check
# Space Complexity: O(n) - stores all elements


class MyQueue:
    def __init__(self):
        """
        Initialize two stacks:
        - stack_in: For enqueue operations (push)
        - stack_out: For dequeue operations (pop/peek)
        """
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        Simply add to input stack - O(1) operation.
        """
        self.stack_in.append(x)

    def pop(self) -> int:
        """
        Remove and return the front element of queue.
        If output stack is empty, transfer all elements from input to output first.
        This reverses the order, making the oldest element (queue front) at the top.
        """
        self._move_in_to_out()
        return self.stack_out.pop()

    def peek(self) -> int:
        """
        Get the front element without removing it.
        Same logic as pop, but just return without removing.
        """
        self._move_in_to_out()
        return self.stack_out[-1]

    def empty(self) -> bool:
        """
        Check if queue is empty.
        Both stacks must be empty for the queue to be empty.
        """
        return len(self.stack_in) == 0 and len(self.stack_out) == 0

    def _move_in_to_out(self) -> None:
        """
        Helper method: Transfer all elements from input stack to output stack.
        This reverses the order, converting LIFO to FIFO.

        Why this works:
        - Input stack: [1, 2, 3] (top is 3, bottom is 1)
        - After transfer: Output stack: [3, 2, 1] (top is 1, which is the front of queue)
        - Now we can pop 1 (the oldest element) first, maintaining FIFO order
        """
        if len(self.stack_out) == 0:
            while len(self.stack_in) > 0:
                self.stack_out.append(self.stack_in.pop())


# Test cases
if __name__ == "__main__":
    # Test case 1: Basic operations
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print(queue.peek())  # Output: 1 (front element)
    print(queue.pop())  # Output: 1 (removed)
    print(queue.empty())  # Output: False

    # Test case 2: Interleaved push and pop
    queue2 = MyQueue()
    queue2.push(1)
    queue2.push(2)
    queue2.push(3)
    print(queue2.pop())  # Output: 1
    print(queue2.pop())  # Output: 2
    queue2.push(4)  # Add new element
    print(queue2.pop())  # Output: 3 (FIFO order maintained)
    print(queue2.pop())  # Output: 4
    print(queue2.empty())  # Output: True

    # Test case 3: Edge case - empty queue
    queue3 = MyQueue()
    print(queue3.empty())  # Output: True
