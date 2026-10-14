class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Brute Fore O(n^2)

        # res = 0
        # store = set(nums)
        # for num in nums:
        #     streak = 0
        #     curr = num
        #     while curr in store:
        #         streak += 1
        #         curr += 1
        #     res =  max(res, streak)
        # return res


        # --- Sorting -- O(n log n)


        # if not nums:
        #     return 0
        
        # nums.sort()
        # longest_streak = 1
        # curr_streak = 1
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         continue
        #     if nums[i] == nums[i-1] + 1:
        #         curr_streak +=1
        #     else:
        #         longest_streak = max(longest_streak, curr_streak)
        #         curr_streak = 1
        # return max(longest_streak, curr_streak)

        # ----- HashSet -----
        numset = set(nums)
        longest = 0
        for num in numset:
            if (num -1) not in numset:
                length = 1
                while(num + length) in numset:
                    length += 1
                longest = max(length, longest)
        return longest