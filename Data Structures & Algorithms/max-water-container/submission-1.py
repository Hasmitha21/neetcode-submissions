class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #Brute Force -- O(n^2)

        # res = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         height = min(heights[i],heights[j])
        #         width = j - i
        #         res = max(res, (height * width))
        
        # return res
        
        # -- TWO POINTERS --

        res = 0
        l = 0
        r = len(heights)-1
        while l < r:
            width = r - l
            height = min(heights[l],heights[r])
            res = max(res, height * width)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res