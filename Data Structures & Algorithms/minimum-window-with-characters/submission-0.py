class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT = {}
        window = {}
        res = [-1,-1]
        reslen = float("inf")
        l = 0

        for c in t:
            countT[c] = 1 + countT.get(c,0)
        
        have = 0
        need = len(countT)

        for r in range(len(s)):
            c = s[r]
            window[c] = 1+ window.get(c,0)
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                #update the result len
                if (r-l+1) < reslen:
                    res = [l,r]
                    reslen = (r-l+1)
                # shriking window from left and removing its occurance by 1 in the window map
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l:r+1] if reslen != float("inf") else ""

        