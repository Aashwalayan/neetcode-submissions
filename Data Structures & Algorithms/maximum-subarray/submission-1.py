class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSoFar = nums[0]
        currMax = nums[0]

        for i in range(1, len(nums)):
            currMax = max(nums[i], nums[i] + currMax)

            maxSoFar = max(maxSoFar, currMax)

        return maxSoFar