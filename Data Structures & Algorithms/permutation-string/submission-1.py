class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        k = len(s1)
        left = 0
        right = k - 1

        while right < len(s2):
            window = "".join(s2[left : right + 1])
            if sorted(window) == sorted(s1):
                return True
            else:
                left += 1
                right +=1

        return False