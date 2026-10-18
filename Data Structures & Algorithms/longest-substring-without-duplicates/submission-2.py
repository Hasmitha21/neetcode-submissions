class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # BRUTE FORCE
        # res = 0
        # for i in range(len(s)):
        #     charSet = set()
        #     # curlen = 0
        #     for j in range(i, len(s)):
        #         if s[j] not in charSet:
        #             # curlen += 1
        #             charSet.add(s[j])
        #         else:
        #             break
        #     res = max(res, len(charSet))
        
        # return res

        # Sliding WINDOW

        charSet = set()

        left = 0
        right = 0
        res = 0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            
            charSet.add(s[right])
            res = max(res, right - left + 1)

        return res