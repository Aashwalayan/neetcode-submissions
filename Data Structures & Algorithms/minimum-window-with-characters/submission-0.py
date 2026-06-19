class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len1 = len(s)
        len2 = len(t)

        if len1 < len2:
            return ""

        countT = [0] * 256
        countS = [0] * 256


        for char in t:
            countT[ord(char)] += 1

        start = 0
        start_idx = -1
        min_len = float('-inf')

        count = 0

        for j in range(len1):

            countS[ord(s[j])] += 1

            if countT[ord(s[j])] != 0 and countS[ord(s[j])] <= countT[ord(s[j])]:
                count += 1
                
            if count == len2:
                while countS[ord(s[start])] > countT[ord(s[start])] or countT[ord(s[start])] == 0:
                    if countS[ord(s[start])] > countT[ord(s[start])]:
                        countS[ord(s[start])] -= 1
                    start += 1


                length = j - start + 1
                if min_len > length:
                    min_len = length
                    start_idx = start


        if start_idx == -1:
            return "-1"

        return s[start_idx:start_idx + min_len]
        
        