// Two Sum
// Two Pointers
// Time Complexity: O(n)
// Space Complexity: O(n)

function twoSum(nums: number[], target: number): number[] {
  const hashMap = new Map();
  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (hashMap.has(complement)) {
      return [hashMap.get(complement), i];
    }

    hashMap.set(nums[i], i)
  }
  return [];
};

console.log(twoSum([2, 7, 11, 15], 9));