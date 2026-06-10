class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        left = 0
        right = n - 1
        water = 0
        result = 0

        while left < right:

            water = min(heights[left], heights[right]) * (right - left)

            result = max(result, water)

            if(heights[left] < heights[right]):
                left += 1
            else:
                right -= 1

        return result