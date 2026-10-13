class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #Brute Force - sorting
        res = defaultdict(list)

        for s in strs:
            sorted_string = ''.join(sorted(s))
            res[sorted_string].append(s)
        
        return list(res.values())