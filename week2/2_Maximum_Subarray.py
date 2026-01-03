# Maximum Subarray
# Kadane's Algorithm (Dynamic Programming)
# Time Complexity: O(n)
# Space Complexity: O(1)

def maxSubArray(nums: list[int]) -> int:
    maxSum = nums[0]
    currentSum = nums[0]
    
    for i in range(1, len(nums)):
        currentSum = max(nums[i], currentSum + nums[i])
        maxSum = max(maxSum, currentSum)
    
    return maxSum

# Test cases
if __name__ == "__main__":
    print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(maxSubArray([1]))  # 1
    print(maxSubArray([5, 4, -1, 7, 8]))  # 23
    print(maxSubArray([-1]))  # -1
    print(maxSubArray([-2, -1]))  # -1
