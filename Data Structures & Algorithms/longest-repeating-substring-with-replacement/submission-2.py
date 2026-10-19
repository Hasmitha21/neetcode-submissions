class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # -- BRUTE FORCE O(n^2)

        # res = 0
        # for i in range(len(s)):
        #     count = {}
        #     maxFreq = 0
        #     for j in range(i, len(s)):
        #         count[s[j]] = 1 + count.get(s[j],0)
        #         maxFreq = max(maxFreq, count[s[j]])
        #         windowLen = j-i+1
        #         if (windowLen - maxFreq) <= k:
        #             res = max(res, windowLen)
        
        # return res


        # --- SLIDING WINDOW ---

        res = 0
        left = 0
        curMax = 0
        count = {}

        for right in range(len(s)):
            
            count[s[right]] = 1 + count.get(s[right],0)
            curMax = max(curMax, count[s[right]])
            # windowlen = right - left + 1
            while ((right - left + 1) - curMax) > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res

