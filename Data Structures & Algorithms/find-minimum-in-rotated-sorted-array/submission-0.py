class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        for i in range(len(nums)):
            if minimum <= nums[i]:
                continue
            else:
                minimum = min(minimum, nums[i])
                return minimum
        return minimum