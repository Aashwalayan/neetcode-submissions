class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S = len(s)
        T = len(t)
        if S != T:
            return False
        for i in range(S):
            if s[i] in t:
                S = S - 1
                t = t.replace(s[i], "", 1)
            else:
                return False
        return True