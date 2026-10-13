class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # if len(s) != len(t):
        #     return False
        
        # return sorted(s) == sorted(t) -- O(nlogn + mlogm)
        if len(s) != len(t):
            return False
        
        smap = {}
        tmap = {}

        for c in s:
            smap[c] = smap.get(c,0) + 1
        
        for c in t:
            tmap[c] = tmap.get(c,0) + 1
        
        return smap == tmap