class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #Brute Force - sorting - O(m*nlogn)
        # res = defaultdict(list)

        # for s in strs:
        #     sorted_string = ''.join(sorted(s))
        #     res[sorted_string].append(s)
        
        # return list(res.values())

        #HashTable

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            res[tuple(count)].append(s)
        
        return list(res.values())