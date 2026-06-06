class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        seen = {}
        for i in range(n):
            key = "".join(sorted(strs[i]))
            if key in seen:
                seen[key].append(strs[i])
            else:
                seen[key] = [strs[i]]
                
        return list(seen.values())