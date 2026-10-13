class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #---- Brute Force Time O(n**2) Space O(1)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
                            
        # return False

        #----- Sorting Time O(nlogn) Space O(n)
        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False

        #-----HashSet Time O(n) Space: O(n)

        check =  set()
        for i in range(len(nums)):
            if nums[i] in check:
                return True
            check.add(nums[i])
        return False