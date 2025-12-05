
#for both positives and negetives
import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum=0
        maxSum= -sys.maxsize - 1
        for i in range(len(nums)):
            currSum+=nums[i]
            maxSum=max(maxSum,currSum)
            if currSum<0:
                currSum=0
        return maxSum


#To print elements
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> tuple[int, List[int]]:
        if not nums:
            return 0, []
        
        currSum = maxSum = nums[0]
        temp_start = start = end = 0
        
        for i in range(1, len(nums)):
            # Try extending current subarray or starting new one
            if nums[i] > currSum + nums[i]:
                currSum = nums[i]
                temp_start = i  # New subarray starts here
            else:
                currSum += nums[i]
            
            # Update max if better
            if currSum > maxSum:
                maxSum = currSum
                start = temp_start
                end = i
        
        # Return sum and elements
        subarray = nums[start:end+1]
        return maxSum, subarray

# Test
sol = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result_sum, elements = sol.maxSubArray(nums)
print(f"Max sum: {result_sum}, Elements: {elements}")  # Output: Max sum: 6, Elements: [4, -1, 2, 1]
