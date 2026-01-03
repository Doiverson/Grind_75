// Implement Queue using Stacks
// Stack
// Time Complexity: O(1)
// Space Complexity: O(n)

class MyQueue {
  private stackIn: number[];
  private stackOut: number[];

  constructor() {
    this.stackIn = [];
    this.stackOut = [];
  }

  push(x: number): void {
    this.stackIn.push(x);
  }

  pop(): number {
    this.moveInToOut();
    return this.stackOut.pop()!;
  }

  peek(): number {
    this.moveInToOut();
    return this.stackOut[this.stackOut.length - 1]!;
  }

  empty(): boolean {
    return this.stackIn.length === 0 && this.stackOut.length === 0;
  }

  private moveInToOut(): void {
    if (this.stackOut.length === 0) {
      while (this.stackIn.length > 0) {
        this.stackOut.push(this.stackIn.pop()!);
      }
    }
  }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */
