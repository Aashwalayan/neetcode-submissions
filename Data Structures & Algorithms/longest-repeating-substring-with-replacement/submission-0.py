class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def getMaxFreq(s, l, r):
            m = {}
            res = 1


            for i in range(l, r + 1):
                m[s[i]] = m.get(s[i], 0) + 1

    
            return res

        def longestSubstr(s, k):
            maxlen = 1
            n = len(s)

            for l in range(n):
                for r in range(l, n):
          
                    f = getMaxFreq(s, l, r)
          
                    if r - l + 1 - f <= k:
                        maxlen = max(maxlen, r - l + 1)
    
            return maxlen