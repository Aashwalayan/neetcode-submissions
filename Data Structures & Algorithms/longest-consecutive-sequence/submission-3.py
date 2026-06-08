class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        st = set()
        res = 0

        for val in nums:
            st.add(val)

        for val in nums:
            if val in st and (val - 1) not in st:

                curr = val
                count = 0

                while curr in st:
                    st.remove(curr)
                    count += 1
                    curr += 1

                res = max(res, count)

        return res
