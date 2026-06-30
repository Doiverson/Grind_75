// Check if All A's Appears Before All B's
// Single Pass
// Time Complexity: O(n)
// Space Complexity: O(1)
// leetcode.com/problems/check-if-all-as-appears-before-all-bs/description/
//
// Best Practice: One left-to-right scan with a seenB flag
// - Valid strings have the form A* B* (all A's, then all B's).
// - If we ever see A after B, return false immediately.
// - A and B may both be absent; that still returns true.

function solution(s: string): boolean {
  let seenB = false;

  for (const ch of s) {
    if (ch === "A" || ch === "a") {
      if (seenB) return false;
    } else if (ch === "B" || ch === "b") {
      seenB = true;
    }
  }

  return true;
}

// Test cases
console.log(solution("aaBBB")); // Expected: true
console.log(solution("ba")); // Expected: false
console.log(solution("aaa")); // Expected: true
console.log(solution("abba")); // Expected: false
console.log(solution("")); // Expected: true
