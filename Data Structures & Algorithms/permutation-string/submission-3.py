class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        k = len(s1)
        left = 0
        right = k - 1
        s1_count = {}

        for i in range(len(s1)):
            if s1[i] in s1_count:
                s1_count[s1[i]] += 1
            else:
                s1_count[s1[i]] = 1

        window_count = {}

        while right < len(s2):
            window = "".join(s2[left : right + 1])
            for i in range(len(window)):
                if window[i] in window_count:
                    window_count[window[i]] += 1
                else:
                    window_count[window[i]] = 1

            if window_count == s1_count:
                return True

            else:
                window_count[s2[left]] -= 1
                if window_count[s2[left]] == 0:
                    del window_count[s2[left]]

                window_count[s2[right + 1]] = window_count.get(s2[right + 1], 0) + 1
                left += 1
                right += 1
                

        return False