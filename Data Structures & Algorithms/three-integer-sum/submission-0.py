class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):

            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    ans.append((nums[i], nums[l], nums[r]))
                    break


        return ans 