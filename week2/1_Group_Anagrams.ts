// Group Anagrams
// Hash Map / Sorting
// Time Complexity: O(n * m log m) where n is number of strings, m is average length
// Space Complexity: O(n * m)
// leetcode.com/problems/group-anagrams/description/

https: const groupAnagrams = (strs: string[]): string[][] => {
  const map = new Map();

  for (const s of strs) {
    const count = new Array(26).fill(0);
    for (const ch of s) {
      count[ch.charCodeAt(0) - 'a'.charCodeAt(0)]++;
    }
    const key = count.join('#'); // 配列はMapキーにしづらいので文字列化
    if (!map.has(key)) map.set(key, []);
    map.get(key).push(s);
  }
  return Array.from(map.values());
};

// Test cases
console.log(groupAnagrams(["eat","tea","tan","ate","nat","bat"]));
console.log(groupAnagrams([""]));
console.log(groupAnagrams(["a"]));
