class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 0
        st = set()
        left = 0

        for i in range(n):
            
            while s[i] in st:
                st.discard(s[left])
                left += 1
                    
            st.add(s[i])

            longest = max(longest, i - left + 1)

        return longest