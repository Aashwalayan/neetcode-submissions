class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        def calc(n):
            num = 0
            n = str(n)
            for i in range(len(n)):
                num += int(n[i]) * int(n[i])
            return num
        
        while n != 1:
            n = calc(n)
            if n in seen:
                return False
            else:
                seen.add(n)
        return True