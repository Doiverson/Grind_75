# Longest Substring Without Repeating Characters
# Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(n)

def lengthOfLongestSubstring(s: str) -> int:
  seen = set()
  l, r = 0, 0
  maxLength = 0

  for r in range(len(s)):
    while s[r] in seen:
      seen.remove(s[l])
      l += 1
    seen.add(s[r])
    maxLength = max(maxLength, r - l + 1)
  return maxLength

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))