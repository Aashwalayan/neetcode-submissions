class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices) - 1
        lowest = prices[0]
        res = 0

        for i in range(1, n):
            lowest = min(lowest, prices[i])

            res = max(res, prices[i] - lowest)

        return res