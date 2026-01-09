// Search a 2D Matrix
// Binary Search (Flatten Approach)
// Time Complexity: O(log(m * n)) where m is rows, n is cols
// Space Complexity: O(1)
// leetcode.com/problems/search-a-2d-matrix/description/
//
// Best Practice: Treat 2D matrix as 1D array
// - Convert 1D index to 2D: row = index / n, col = index % n
// - Single binary search is simpler and more efficient

function searchMatrix(matrix: number[][], target: number): boolean {
  const m = matrix.length; // number of rows
  const n = matrix[0].length; // number of columns
  let left = 0;
  let right = m * n - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    // Convert 1D index to 2D coordinates
    const row = Math.floor(mid / n);
    const col = mid % n;
    const value = matrix[row][col];

    if (value === target) {
      return true;
    } else if (value < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return false;
}

// Test cases
console.log(
  searchMatrix(
    [
      [1, 3, 5, 7],
      [10, 11, 16, 20],
      [23, 30, 34, 60],
    ],
    3
  )
); // true

console.log(
  searchMatrix(
    [
      [1, 3, 5, 7],
      [10, 11, 16, 20],
      [23, 30, 34, 60],
    ],
    13
  )
); // false

console.log(searchMatrix([[1]], 1)); // true
