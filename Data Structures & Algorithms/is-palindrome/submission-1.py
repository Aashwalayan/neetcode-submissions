class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        return False