// Longest Substring Without Repeating Characters
// Sliding Window
// Time Complexity: O(n)
// Space Complexity: O(n)

const lengthOfLongestSubstring = (s: string): number => {
  const seen = new Set();
  let l = 0;
  let maxLength = 0;

  for (let r = 0; r < s.length; r++) {
    while (seen.has(s[r])) {
      seen.delete(s[l]);
      l++;
    }
    seen.add(s[r]);
    maxLength = Math.max(maxLength, r - l + 1);
  }
  return maxLength;
};
console.log(lengthOfLongestSubstring('abcabcbb'));
console.log(lengthOfLongestSubstring('bbbbb'));
console.log(lengthOfLongestSubstring('pwwkew'));
