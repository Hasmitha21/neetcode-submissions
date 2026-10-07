class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0

        # [rob1, rob2, n, n+1, ....]
        for i in nums:
            temp =  max(i + rob1, rob2)
            rob1 = rob2
            rob2 = temp
            # [rob2, max(next subarray)]
        return rob2