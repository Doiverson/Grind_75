# Group Anagrams
# Hash Map / Sorting
# Time Complexity: O(n * m log m) where n is number of strings, m is average length
# Space Complexity: O(n * m)
# leetcode.com/problems/group-anagrams/description/


from collections import defaultdict


def groupAnagrams(strs):
  groups = defaultdict(list)

  for s in strs:
    count = [0] * 26
    for ch in s:
      count[ord(ch) - ord('a')] += 1
    groups[tuple(count)].append(s)
  return list(groups.values())

# Test cases
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))
