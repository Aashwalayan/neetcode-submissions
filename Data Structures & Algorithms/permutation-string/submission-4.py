class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

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

        # Build first window once
        for i in range(k):
            if s2[i] in window_count:
                window_count[s2[i]] += 1
            else:
                window_count[s2[i]] = 1

        while True:

            if window_count == s1_count:
                return True

            if right == len(s2) - 1:
                break

            window_count[s2[left]] -= 1
            if window_count[s2[left]] == 0:
                del window_count[s2[left]]

            window_count[s2[right + 1]] = window_count.get(s2[right + 1], 0) + 1

            left += 1
            right += 1

        return False