class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        def calc(n):
            return sum(int(digit) ** 2 for digit in str(n))
        
        while n != 1:
            n = calc(n)
            if n in seen:
                return False
            else:
                seen.add(n)
        return True