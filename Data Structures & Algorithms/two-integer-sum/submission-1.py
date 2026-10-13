class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Brute Force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        nums_map = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in nums_map:
                return [nums_map[complement],i]
            nums_map[n] = i