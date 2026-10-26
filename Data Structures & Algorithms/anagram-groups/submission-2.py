class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_map = defaultdict(list)
        for i in range(len(strs)):
            sorted_str = "".join(sorted(strs[i]))
            strs_map[sorted_str].append(strs[i])
        
        return list(strs_map.values())