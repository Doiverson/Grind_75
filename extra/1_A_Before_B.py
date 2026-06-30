# Check if All A's Appears Before All B's
# Single Pass
# Time Complexity: O(n)
# Space Complexity: O(1)
# leetcode.com/problems/check-if-all-as-appears-before-all-bs/description/
#
# Best Practice: One left-to-right scan with a seen_b flag
# - Valid strings have the form A* B* (all A's, then all B's).
# - If we ever see A after B, return False immediately.
# - A and B may both be absent; that still returns True.


def solution(s: str) -> bool:
    seen_b = False

    for ch in s:
        if ch in ("A", "a"):
            if seen_b:
                return False
        elif ch in ("B", "b"):
            seen_b = True

    return True


# Test cases
if __name__ == "__main__":
    print(solution("aaBBB"))  # Expected: True
    print(solution("ba"))  # Expected: False
    print(solution("aaa"))  # Expected: True
    print(solution("abba"))  # Expected: False
    print(solution(""))  # Expected: True
