# Valid Anagram
# Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

def isValidAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False

    return True

print(isValidAnagram("anagram", "nagaram"))