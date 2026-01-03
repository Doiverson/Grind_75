# Valid Parentheses
# Stack
# Time Complexity: O(n)
# Space Complexity: O(n)

def isValid(s: str) -> bool:
    m = []
    brackets = ['(', '{', '[']
    closed = [')', '}', ']']

    for char in s:
        if char in closed:
            if len(m) == 0:
                return False

            if m[-1] == brackets[closed.index(char)]:
                m.pop()
            else:
                return False
        else:
            m.append(char)

    if len(m) == 0:
        return True
    return False

# Test cases
if __name__ == "__main__":
    print(isValid('()'))
    print(isValid('()[]{}'))
    print(isValid('(]'))
    print(isValid('([)]'))
    print(isValid('{[]}'))
    print(isValid(''))
