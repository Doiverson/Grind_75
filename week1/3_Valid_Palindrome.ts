// Valid Palindrome
// Two Pointers
// Time Complexity: O(n)
// Space Complexity: O(1)

const isPalindrome = (s: string): boolean => {
  let l = 0;
  let r = s.length - 1;

  const isAlphaNum = (ch: string) => /[0-9a-zA-Z]/.test(ch);

  while (l < r) {
    while (l < r && !isAlphaNum(s[l])) l++;
    while (l < r && !isAlphaNum(s[r])) r--;
    if (s[l].toLowerCase() !== s[r].toLowerCase()) return false;
    l++
    r--
  }

  return true;
}

console.log(isPalindrome("A man, a plan, a canal: Panama"));