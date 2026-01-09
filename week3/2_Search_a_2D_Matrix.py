# Search a 2D Matrix
# Binary Search (Flatten Approach)
# Time Complexity: O(log(m * n)) where m is rows, n is cols
# Space Complexity: O(1)
# leetcode.com/problems/search-a-2d-matrix/description/
#
# Best Practice: Treat 2D matrix as 1D array
# - Convert 1D index to 2D: row = index // n, col = index % n
# - Single binary search is simpler and more efficient

from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    m = len(matrix)  # number of rows
    n = len(matrix[0])  # number of columns
    left = 0
    right = m * n - 1

    while left <= right:
        mid = (left + right) // 2
        # Convert 1D index to 2D coordinates
        row = mid // n
        col = mid % n
        value = matrix[row][col]

        if value == target:
            return True
        elif value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# Test cases
if __name__ == "__main__":
    print(
        searchMatrix(
            [
                [1, 3, 5, 7],
                [10, 11, 16, 20],
                [23, 30, 34, 60],
            ],
            3,
        )
    )  # True

    print(
        searchMatrix(
            [
                [1, 3, 5, 7],
                [10, 11, 16, 20],
                [23, 30, 34, 60],
            ],
            13,
        )
    )  # False

    print(searchMatrix([[1]], 1))  # True
