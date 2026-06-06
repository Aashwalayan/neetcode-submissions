class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S = sorted(s)
        T = sorted(t)
        if len(S) != len(T):
            return False
        for i in range(len(S)):
            if S[i] == T[i]:
                continue
            else:
                return False
        return True