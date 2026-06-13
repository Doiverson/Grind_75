# Find Minimum in Rotated Sorted Array
# Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)
# leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# Best Practice: Compare mid against the right boundary, not the neighbors
# - The rotated array is two ascending blocks; every value in the left block
#   is larger than every value in the right block.
# - nums[right] always belongs to the smaller (right) block, so it is a stable
#   reference point that also handles the non-rotated case naturally.
# - Shrink the range toward the smaller block until left == right.

from typing import List


def findMin(nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1

    # Converge the range to a single index (the minimum).
    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            # mid sits in the larger (left) block, so the minimum must be to
            # the right of mid. mid itself cannot be the answer; discard it.
            left = mid + 1
        else:
            # mid sits in the smaller (right) block, so the minimum is mid or
            # to its left. Keep mid as a candidate.
            right = mid

    # left == right now points at the inflection point: the minimum.
    return nums[left]


# Test cases
if __name__ == "__main__":
    print(findMin([3, 4, 5, 1, 2]))        # Expected: 1
    print(findMin([4, 5, 6, 7, 0, 1, 2]))  # Expected: 0
    print(findMin([11, 13, 15, 17]))       # Expected: 11
