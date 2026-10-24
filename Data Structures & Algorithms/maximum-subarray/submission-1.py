class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # BRUTE FORCE

        # res = nums[0]

        # for i in range(len(nums)):
        #     cursum = 0
        #     for j in range(i, len(nums)):
        #         cursum += nums[j]
        #         res = max(res, cursum)
        
        # return res

        # KADANE'S ALGORITHM
        maxSubarr = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSubarr = max(maxSubarr, curSum)
        
        return maxSubarr