class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        n = len(nums)

        for i in range(n):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        
        def get_frequency(item):
            return item[1]

        result = sorted(freq.items(), key = get_frequency, reverse = True)
        
        ans = []

        for item in result[:k]:
            ans.append(item[0])

        return ans