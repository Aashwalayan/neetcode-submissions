class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def check(piles, mid, h):
            totalHours = 0
            for i in range(len(piles)):
                totalHours += (piles[i] + mid - 1) // mid

            return totalHours <= h

        low = 1
        high = max(piles)

        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if check(piles, mid, h):
                hi = mid - 1
                res = mid

            else:
                lo = mid + 1

        return ans