class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1, rob2 = 0,0

        # # [rob1, rob2, n, n+1, ....]
        # for i in nums:
        #     temp =  max(i + rob1, rob2)
        #     rob1 = rob2
        #     rob2 = temp
        #     # [rob2, max(next subarray)]
        # return rob2

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp =[0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[len(nums)-1]