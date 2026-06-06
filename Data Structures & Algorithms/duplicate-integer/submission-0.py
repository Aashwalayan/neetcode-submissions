class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        n = len(nums)

        for i in range(n):
            if nums[i] in seen:
                return True
            else:
                seen[nums[i]] = i
        return False