class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maximum = float('-inf')
        result = []
        left = 0
        right = left + k - 1

        while left <= right:
            maximum = max(maximum, nums[left])
            left += 1
        result.append(maximum)
        maximum = 0
            
        left = 1
        right += 1

        while right < (len(nums)):
            if nums[right] >= maximum:
                result.append(nums[right])
                
            else:
                temp = right
                while right >= left:
                    maximum = max(maximum, nums[right])
                    right -= 1
                result.append(maximum)
                maximum = 0
                right = temp + 1
            
            left += 1
            right += 1

        return result

            
