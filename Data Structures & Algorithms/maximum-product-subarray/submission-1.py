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
        # res = max(nums)
        # currMin, currMax = 1, 1
        # for n in nums:
        #     # if n == 0:
        #     #     continue
        #     temp = currMax * n

        #     currMax = max(n * currMax, n * currMin, n)
        #     currMin = min(temp, n * currMin, n)
        #     res = max(res,currMax)
        # return res

        res = nums[0]
        prefix = 0
        suffix = 0
        for i in range(len(nums)):
            prefix = nums[i] * (prefix if prefix!=0 else 1)
            suffix = nums[len(nums)-1-i] * (suffix if suffix!=0 else 1)
            res = max(res, prefix, suffix)
        return res