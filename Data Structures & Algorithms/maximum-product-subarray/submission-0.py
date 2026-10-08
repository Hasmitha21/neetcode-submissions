class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # res = nums[0]

        # for i in range(len(nums)):
        #     curr = nums[i]
        #     res = max(res,curr)
        #     for j in range(i+1,len(nums)):
        #         curr *= nums[j]
        #         res = max(res,curr)
        # return res. ---- O(n^2)
        res = max(nums)
        currMin, currMax = 1, 1
        for n in nums:
            # if n == 0:
            #     continue
            temp = currMax * n

            currMax = max(n * currMax, n * currMin, n)
            currMin = min(temp, n * currMin, n)
            res = max(res,currMax)
        return res



        