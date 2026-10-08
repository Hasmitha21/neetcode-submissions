class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lengths = [1] * len(nums)
        for i in range(1, len(nums)):
            for k in range(i):
                if nums[k] < nums[i]:
                    lengths[i] = max(lengths[i], lengths[k]+1)
        return max(lengths)
        