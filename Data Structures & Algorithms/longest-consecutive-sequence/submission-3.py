class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # if not nums:
        #     return 0
        # res = 0
        # nums.sort()

        # curr = nums[0]
        # streak = 0

        # for i in range(len(nums)):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     if curr != nums[i]:
        #         curr = nums[i]
        #         streak = 0
            
        #     streak += 1
        #     curr += 1
        #     res = max(res, streak)
        
        # return res
        
        numSet = set(nums)
        streak = 0
        for num in numSet:
            if num-1 not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                streak = max(streak, length)
        
        return streak
                

