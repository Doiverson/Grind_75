// Best Time to Buy and Sell Stock
// Two Pointers / Sliding Window
// Time Complexity: O(n)
// Space Complexity: O(1)
// leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
//
// Best Practice: Single pass, track the cheapest price seen so far
// - Buy low, sell high: profit only exists when selling after a cheaper day.
// - Sweep left to right while remembering the minimum price (buy candidate).
// - At each day, the best sell-today profit is price - minPrice.

function maxProfit(prices: number[]): number {
  let minPrice = Infinity; // cheapest buy price seen so far
  let maxProfit = 0;

  for (const price of prices) {
    if (price < minPrice) {
      // Found a cheaper day to buy; update the buy candidate.
      minPrice = price;
    } else {
      // Selling today; keep the best profit seen.
      maxProfit = Math.max(maxProfit, price - minPrice);
    }
  }

  return maxProfit;
}

// Test cases
console.log(maxProfit([7, 1, 5, 3, 6, 4])); // Expected: 5
console.log(maxProfit([7, 6, 4, 3, 1]));    // Expected: 0
