// Valid Parentheses
// Stack
// Time Complexity: O(n)
// Space Complexity: O(n)

const isValid = (s: string): boolean => {
  let m: string[] = [];
  let brackets = ['(', '{', '['];
  let closed = [')', '}', ']'];

  for (let i = 0; i < s.length; i++) {
    if (closed.includes(s[i])) {
      if (m.length === 0) return false;

      if (m[m.length - 1] === brackets[closed.indexOf(s[i])]) {
        m.pop();
      } else {
        return false;
      }
    } else {
      m.push(s[i]);
    }
  }
  if (m.length === 0) return true;
  return false;
};

// Test cases
console.log(isValid('()'));
console.log(isValid('()[]{}'));
console.log(isValid('(]'));
console.log(isValid('([)]'));
