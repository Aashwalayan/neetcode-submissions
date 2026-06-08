class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        p = ""

        for i in range(n):
            if s[i].isalnum():
                p += s[i]
            else:
                continue

        
        i = 0
        j = len(p) - 1 


        while i < j:
            if p[i].lower() != p[j].lower():
                return False
            else:
                i = i + 1
                j = j - 1
        return True