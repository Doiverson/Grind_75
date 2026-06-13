# Best Time to Buy and Sell Stock
# Two Pointers / Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)
# leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# Best Practice: Single pass, track the cheapest price seen so far
# - Buy low, sell high: profit only exists when selling after a cheaper day.
# - Sweep left to right while remembering the minimum price (buy candidate).
# - At each day, the best sell-today profit is price - min_price_so_far.

from typing import List


def maxProfit(prices: List[int]) -> int:
    min_price = float("inf")  # cheapest buy price seen so far
    max_profit = 0

    for price in prices:
        if price < min_price:
            # Found a cheaper day to buy; update the buy candidate.
            min_price = price
        else:
            # Selling today; keep the best profit seen.
            max_profit = max(max_profit, price - min_price)

    return max_profit


# Test cases
if __name__ == "__main__":
    print(maxProfit([7, 1, 5, 3, 6, 4]))  # Expected: 5
    print(maxProfit([7, 6, 4, 3, 1]))     # Expected: 0
